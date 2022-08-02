from functools import wraps
from flask import redirect, session, flash
from datetime import datetime

# Define photo extentions allowed for upload in publish.html or /my_blog/publish
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# Decorate routes to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


# Function to check photo file extentions for use in /my_blog/publish
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Return file extention as string
def extention(filename):
    return ".{extention}".format(extention=filename.rsplit('.', 1)[1].lower())


# Return current date time as string
def date_time():

    # Date time format
    fmt = "%d-%m-%Y %H:%M:%S"

    # Turn date time variable into string and apply format
    dt_now = datetime.now().strftime(fmt)

    return dt_now