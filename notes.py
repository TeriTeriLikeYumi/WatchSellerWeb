import os,datetime
from flask import (Flask, Blueprint, abort,
                   render_template,redirect, current_app,
                   url_for, flash, request,session)
from flask_login import (login_user, current_user,
                         logout_user, login_required)
from jinja2 import TemplateNotFound

from libs.User import User

notes_app = Blueprint('notes_app', __name__,template_folder='templates')

@notes_app.route('/')
def index():
    if 'username' in session:
        return redirect('/home')
    return render_template('layout.html', is_home=True)

@notes_app.route('/home')
@login_required
def home():
    return render_template('layout.html', is_home=True)

'''@notes_app.route('/add_to_cart/<int:product_id>', methods=['GET','POST'])
@login_required

def add_to_cart(product_id):
    product = models.Product.query.get(product_id)
    if product is None:
        abort(404)
    return render_template('add_to_cart.html', product=product)
'''
@notes_app.route('/shopping_cart')
@login_required
def shopping_cart():
    return render_template('shopping_cart.html')