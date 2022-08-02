return import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, date_time

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Retrieve from portfolio in finance.db stocks that belong to user
    portfolio = db.execute("SELECT * FROM portfolio WHERE user_id = :user_id", user_id=session["user_id"])

    # Update current price for each stock row
    for stock in portfolio:
        quote = lookup(stock["symbol"])
        stock["current_price"] = quote["price"]

    # Retrieve from users table in finance.db user's cash
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cash = user[0]["cash"]

    # Calculate total balance
    total = cash
    for stock in portfolio:
        total += stock["current_price"] * stock["shares"]

    # Display portfolio table for GET route
    return render_template("index.html", portfolio=portfolio, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If buy request submitted via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("shares must be a posative integer", 400)

        # Error checking user input
        if not symbol:
            return apology("please provide symbol")
        if not shares:
            return apology("please provide shares quantity")

        # Look up share price
        quote_dict = lookup(symbol)
        if not quote_dict:
            return apology("invalid symbol")
        if int(shares) <= 0:
            return apology("invalid shares quantity")

        # Record transaction data
        price = quote_dict["price"]
        name = quote_dict["name"]
        symbol = quote_dict["symbol"]
        datetime_str = date_time()

        # Obtain cash from users table in finance.db
        user_id = session["user_id"]
        users_dict = db.execute("SELECT * FROM users WHERE id = ?", user_id)
        cash = users_dict[0]["cash"]

        # Check if user has enough cash for stock purchase
        if cash < float(price) * int(shares):
            return apology("insufficient cash")

        # Update cash in users table
        cash -= float(price) * int(shares)
        cash_update = db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

        # Log buy request into transactions table in finance.db
        transaction_id = db.execute("INSERT INTO transactions (symbol, name, shares, price, datetime_str, user_id) VALUES (:symbol, :name, :shares, :price, :datetime_str, :user_id)",
            symbol=symbol, name=name, shares=shares, price=price, datetime_str=datetime_str, user_id=user_id)

        # Log buy request into portfolio table in finance.db
        stock = db.execute("SELECT * FROM portfolio WHERE user_id = :user_id AND symbol = :symbol", user_id=user_id, symbol=symbol)
        # if stock already exists in portfolio, update shares quantity
        if len(stock) == 1:
            new_shares = int(stock[0]["shares"]) + int(shares)
            db.execute("UPDATE portfolio SET shares = :shares WHERE user_id = :user_id AND symbol = :symbol",
                shares=new_shares, user_id=user_id, symbol=symbol)
        # else if stock is new, insert new row into portfolio
        else:
            portfolio_id = db.execute("INSERT INTO portfolio (user_id, symbol, name, shares) VALUES(:user_id, :symbol, :name, :shares)",
                user_id=user_id, symbol=symbol, name=name, shares=shares)

        # Redirect to index page for POST route
        return redirect("/")

    # GET route
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Obtain transactions from transactions table in finance.db belonging to user
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])

    # Display transactions table
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # If user requests quotation via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Error Checking user input
        if not symbol:
            return apology("please provide symbol")
        quote_dict = lookup(symbol)
        if not quote_dict:
            return apology("invalid symbol")

        # Via POST & valid symbol entered
        return render_template("quoted.html", name=quote_dict["name"], price=usd(quote_dict["price"]), symbol=quote_dict["symbol"])

    # Via GET
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User submits registration via POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Error checking for registration inputs
        if not username:
            return apology("please provide username")
        if not password:
            return apology("please provide password")
        if not confirmation:
            return apology("please confirm password")
        if confirmation != password:
            return apology("passwords do not match")

        # Ensure unique username
        if db.execute("SELECT * FROM users WHERE username = (?)", username):
            return apology("username taken")

        # Add registrant into user table then redirect to login
        user_id = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
            username=username, hash=generate_password_hash(password))
        return redirect("/login")

    # Via GET
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # If sell request via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("shares must be a posative integer", 400)
        user_id = session["user_id"]

        # Error checking user input
        if not symbol:
            return apology("please select symbol")
        if not shares:
            return apology("please provide shares quantity")
        if shares <= 0:
            return apology("invalid shares quantity")

        quote = lookup(symbol)
        if not quote:
            return apology("transaction error")

        # Record transaction data
        price = quote["price"]
        name = quote["name"]
        symbol = quote["symbol"]
        datetime_str = date_time()

        # Check if user owns the stock
        stock = db.execute("SELECT * FROM portfolio WHERE user_id = :user_id AND symbol = :symbol", user_id=user_id, symbol=symbol)
        if not stock:
            return apology("you do not own this stock")

        # Check if user owns sufficient shares
        if int(stock[0]["shares"]) < int(shares):
            return apology("you do not own sufficient shares")

        # Log into transactions table in finance.db
        db.execute("INSERT INTO transactions (symbol, name, shares, price, datetime_str, user_id) VALUES (:symbol, :name, :shares, :price, :datetime_str, :user_id)",
            symbol=symbol, name=name, shares=(- int(shares)), price=price, datetime_str=datetime_str, user_id=user_id)

        # Log into portfolio table in finance.db
        if int(stock[0]["shares"]) == int(shares):
            db.execute("DELETE FROM portfolio WHERE user_id = :user_id AND symbol = :symbol", user_id=user_id, symbol=symbol)
        else:
            db.execute("UPDATE portfolio SET shares = :shares WHERE user_id = :user_id AND symbol = :symbol",
                shares=(int(stock[0]["shares"]) - int(shares)), user_id=user_id, symbol=symbol)

        # Update cash in users table in finance.db
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)
        cash = user[0]["cash"]
        cash += int(shares) * float(price)
        db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash=cash, user_id=user_id)

        # Redirect to index for POST route
        return redirect("/")

    # Via GET
    portfolio = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])
    return render_template("sell.html", portfolio=portfolio)


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change user's password"""

    # User reached route via POST
    if request.method == "POST":

        # Variables from user input
        username = request.form.get("username")
        old_password = request.form.get("old-password")
        new_password = request.form.get("new-password")
        confirmation = request.form.get("confirmation")

        # Ensure inputs not empty
        if not username:
            return apology("must provide username", 403)
        elif not old_password:
            return apology("must provide old password", 403)
        elif not new_password:
            return apology("must provide new password")
        elif not confirmation:
            return apology("must confirm new password")

        # Check user login details using old password (security)
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], old_password):
            return apology("invalid username and/or password", 403)

        # Check if confirmation equals new password
        if confirmation != new_password:
            return apology("confirmation does not match new password")

        # Log new password into users table in finance.db
        db.execute("UPDATE users SET hash = :hash WHERE id = :user_id",
            user_id=session["user_id"], hash=generate_password_hash(new_password))

        # Redirect user to home page
        return redirect("/")

    # GET route
    return render_template("change-password.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
