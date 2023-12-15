from flask import (Blueprint, render_template,redirect, 
                   flash, request, url_for)

from flask_login import login_user, logout_user, login_required

from libs.User import User
from libs.forms import RegisterForm, LoginForm
from app import flask_bcrypt,login_manager

auth_app = Blueprint('auth_app', __name__,template_folder='templates')

@auth_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = auth_app.config['USERS_COLLECTION'].find_one({'username': form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['username'])
            
            login_user(user_obj)
            flash('Logged in successfully.', 'success')
            return redirect("/home")
        flash('Invalid username or password.', 'danger')   
    return render_template('login.html', form=form, current_page='login')

    
@auth_app.route("/logout")
@login_required
def logout():
        """Log user out"""
    
        logout_user()
        flash('You have been logged out.', 'success')
        # Redirect user to login form
        return redirect("/login")
    
@auth_app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        # Get Form Fields
        username = form.username.data
        password = form.password.data
        # Hash password
        password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
        # Create user
        auth_app.config['USERS_COLLECTION'].insert_one({'username': username, 'password': password_hash})
        # Flash message
        flash('You are now registered and can log in', 'success')
        # Redirect to login page
        return redirect("/login")
    return render_template('register.html', form=form, current_page='register')

@login_manager.user_loader
def load_user(username):
    u = auth_app.config['USERS_COLLECTION'].find_one({'username': username})
    if not u:
        return None
    return User(u['username'])