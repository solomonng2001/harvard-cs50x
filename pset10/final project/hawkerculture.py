import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

from helpers import login_required, allowed_file, extention, date_time

# Configure application
app = Flask(__name__)

# Configure photo upload folder & maximum file size in bytes
UPLOAD_FOLDER = '/home/ubuntu/project/static/photos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure templates aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-chache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///hawkerculture.db")


@app.route("/")
def index():

    # Extract user's posts from posts table in hawkerculture.db
    posts = db.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 20")

    # Extract url for photos file
    photo_url = UPLOAD_FOLDER.split("/home/ubuntu/project", 1)[1]

    # Display all user's blog posts via GET
    return render_template("index.html", posts=posts, photo_url=photo_url)

@app.route("/search", methods=["GET", "POST"])
def search():

    # POSTS route
    if request.method == "POST":

        # Extract all posts where title, location, tags, contain keywords of search
        posts = db.execute("SELECT * FROM posts WHERE title LIKE :search OR address LIKE :search OR tags LIKE :search LIMIT 20", search="%{}%".format(request.form.get("search")))

        # Notify if search not successful
        if not posts:
            flash("Your search did not match any post.")

        # Extract url for photos file
        photo_url = UPLOAD_FOLDER.split("/home/ubuntu/project", 1)[1]

        # Display searched posts
        return render_template("index.html", posts=posts, photo_url=photo_url)

    # Else if via GET route
    return redirect("/")


@app.route("/my_blog")
@login_required
def my_blog():

    # Extract user's posts from posts table in hawkerculture.db
    posts = db.execute("SELECT * FROM posts WHERE user_id = ? ORDER BY id DESC", session["user_id"])

    # Extract url for photos file
    photo_url = UPLOAD_FOLDER.split("/home/ubuntu/project", 1)[1]

    # Display all user's blog posts via GET
    return render_template("my_blog.html", posts=posts, photo_url=photo_url)


# Post/publish blog
@app.route("/publish", methods=["GET", "POST"])
@login_required
def publish():

    # Via POST
    if request.method == "POST":

        # Remember inputs
        session["title"] = request.form.get("title")
        session["address"] = request.form.get("address")
        session["review"] = request.form.get("review")
        session["tags"] = request.form.get("tags")

        # Ensure necessary fields are not empty
        flash_count = 0
        if not session["title"]:
            flash("Please provide Blog Title / Stall Name.")
            flash_count += 1
        #if not request.form.get("photos"):
            #flash("Please upload photos.")
            #flash_count += 1
        if not session["address"]:
            flash("Please provide Address.")
            flash_count += 1
        if not session["review"]:
            flash("We would love to hear your review.")
            flash_count += 1
        if not session["tags"]:
            flash("Please tag cuisine type.")
            flash_count += 1

        # Check if photos uploaded
        files = request.files.getlist('photos')
        if not files:
            flash("Please upload photos.")
            flash_count += 1

        # Check file extention for photos if uploaded
        else:
            for file in files:
                if not allowed_file(file.filename):
                    flash("Incompatible file type.")
                    flash_count += 1

        # If no errors, log into posts table in hawkerculture.db
        if flash_count == 0:
            post_id = db.execute("INSERT INTO posts (user_id, title, tags, date_time, address, review) VALUES (:user_id, :title, :tags, :date_time, :address, :review)", user_id=session["user_id"], title=session["title"], tags=session["tags"], date_time=date_time(), address=session["address"], review=session["review"])

            # Save photos in upload path
            file_count = 0
            filename_list = []
            for file in files:
                filename = "post{post_id}_photo{file_count}{extention}".format(post_id=post_id, file_count=file_count, extention=extention(file.filename))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filename_list.append(filename)
                file_count += 1

            # Append assigned filename into posts table in hawkerculture.db
            db.execute("UPDATE posts SET photo_id = :photo_id WHERE id = :post_id", photo_id=str(filename_list), post_id=post_id)

            # Redirect back to user's blog posts and notify success of published post
            flash("Blog successfully published.")
            return redirect("/my_blog")

        # Return form with user inputs retained
        return render_template("publish.html", title=session["title"], address=session["address"], review=session["review"], tags=session["tags"])

    # Via GET with user inputs of value null
    return render_template("publish.html", title="", address="", review="", tags="")


# Log user in
@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    # Via POST
    if request.method == "POST":

        # Ensure username & password
        if not request.form.get("username"):
            flash("Please provide username.")
        elif not request.form.get("password"):
            flash("Please provide password.")

        # Check if username exists and password correct
        else:
            user = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
            if len(user) != 1 or not check_password_hash(user[0]["hash"], request.form.get("password")):
                flash("Invalid username and/or password.")
            else:

                # Remember user that logged in
                session["user_id"] = user[0]["id"]

                # Redirect to home page if user logged in successfully
                return redirect("/")

    # Via GET route & wrong password/username
    return render_template("login.html")


# Create user account
@app.route("/create_account", methods=["GET", "POST"])
def create_account():

    # Via POST
    if request.method == "POST":

        # Error checking: username, password, confirmation, matching passwords, unique username
        if not request.form.get("username"):
            flash("Please provide username.")
        elif not request.form.get("password"):
            flash("Please provide password.")
        elif not request.form.get("confirmation"):
            flash("Please confirm password.")
        elif request.form.get("confirmation") != request.form.get("password"):
            flash("Passwords do not match.")
        elif db.execute("SELECT * FROM users WHERE username = (?)", request.form.get("username")):
            flash("Username taken. Please provide another username.")

        # Add new account into users table
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
            return redirect("/")

    # Via GET or errors detected
    return render_template("create_account.html")


# Log user out
@app.route("/logout")
@login_required
def logout():

    # Forget user
    session.clear()

    # Redirect to login
    return redirect("/")

# If file uploaded on my_blog.html via /my_blog/publish is too large
@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413