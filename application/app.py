from flask import Response, Flask, flash
from flask import redirect, render_template, request, session

from flask_session import Session

from werkzeug.utils import secure_filename
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

import pymongo
import uuid

app = Flask(__name__)
app.secret_key = b'\x1d\xd2\x14\xea\xe3M\x1d\x96\x8e\xf5\x05)\xee\x9e\x99\x05'

# DATABASE CONNECTION
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.users_login_system

# CONFIGURE FLASK-SESSION
from tempfile import mkdtemp

# ENSURE TEMPLATES ARE AUTO-RELOADED
app.config["TEMPLATES_AUTO_RELOAD"] = True

# ENSURE RESPONSES AREN'T CACHED
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# CONFIGURE SESSION TO USE FILESYSTEM (INSTEAD OF SIGNED COOKIES)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# IMPORTS
from helpers import login_required, apology

@app.route('/')
@login_required
def home():
    return render_template('face.html')

@app.route('/home')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])     
def login():
    """Log user in"""
        
    # FORGET ANY USER_ID
    session.clear()
        
    # USER REACHED ROUTE VIA POST
    if request.method == "POST":
        # ASSIGN VARIABLES
        input_username = request.form.get("username")
        input_password = request.form.get("password")
            
        # ENSURE USERNAME WAS SUBMITTED
        if not input_username:
            return render_template("login.html", messenge = 1)
            
        # ENSURE PASSWORD WAS SUBMITTED
        elif not input_password:
            return render_template("login.html", messenge = 2)
            
        # QUERY DATABASE FOR USERNAME
        user = db.users.find_one({ "username": input_username })
            
        # ENSURE USERNAME EXISTS AND PASSWORD IS CORRECT
        if user and check_password_hash(user["password"], input_password):
            # KEEP USER LOGGED IN
            session["user_id"] = user["_id"]   
                
            # REDIRECT USER TO HOMEPAGE
            return redirect("/")
        else:
            return render_template("login.html", messenge = 3)
            
        # USER REACHED ROUTE VIA GET
    else:
        return render_template("login.html", messenge = 3)

@app.route('/logout')    
def logout():
    """Log user out"""
        
    # FORGET ANY USER_ID
    session.clear()
        
    # REDIRECT USER TO LOGIN FORM
    return redirect("/")


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    
    # USER REACHED ROUTE VIA POST
    if request.method == "POST":
        #ASSIGN VARIABLES
        input_username = request.form.get("username")
        input_password = request.form.get("password")
        input_confirmation = request.form.get("confirmation")
        
        # ENSURE USERNAME WAS SUBMITTED
        if not input_username:
            return render_template("register.html", messenge = 1)
    
        # ENSURE PASSWORD WAS SUBMITTED
        elif not input_password:
            return render_template("register.html", messenge = 2)
    
        # ENSURE CONFIRMATION WAS SUBMITTED
        elif not input_confirmation:
            return render_template("register.html", messenge = 4)
    
        elif input_password == input_confirmation:
            return render_template("register.html", messenge = 3)
    
    
        # CREATE USER OBJECT
        user = {
             "_id": uuid.uuid4().hex,
              "username": input_username,
              "password": input_password
              }
    
        # ENSURE USERNAME IS UNIQUE
        if db.users.find_one({ "username": user['username'] }):
             return render_template("register.html", messenge=5)
    
            # QUERY DATABASE FOR NEW USER
        else:
            new_user = db.users.insert_one(user)
            if new_user.acknowledged:
                # KEEP USER LOGGED IN
                session["user_id"] = user["_id"]
                flash(f"Registered as {user['username']}", "success")
                return redirect("/")
            
            else:
                # FAILED TO CREATE USER
                return render_template("register.html", messenge="FAIL")
            
    # USER REACHED ROUTE VIA GET
    else:
        return render_template("register.html")
                 
@app.errorhandler(InternalServerError)
def handle_internal_server_error(e):
    return render_template('error.html', e=e)

@app.errorhandler(NotFound)
def handle_not_found_error(e):
    return render_template('error.html', e=e)

if __name__ == '__main__':
    app.run()