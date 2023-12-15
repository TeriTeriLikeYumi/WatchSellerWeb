from flask import Flask

from flask_login import LoginManager
from flask_pymongo import PyMongo


# DATABASE CONNECTION
app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x1d\xd2\x14\xea\xe3M\x1d\x96\x8e\xf5\x05)\xee\x9e\x99\x05'
app.config['MONGO_URI'] = 'mongodb+srv://Admin:7d8OMUFQX6Tls1C9@cluster1.iwwrtht.mongodb.net/'


# MONGO DB CONNECTION
mongodb_client = PyMongo(app)
db = mongodb_client.db


# FLASK-BCRYPT 
from flask_bcrypt import Bcrypt
flask_bcrypt = Bcrypt(app)

# ASSOCIATE FLASK-LOGIN WITH FLASK APP
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_app.login'