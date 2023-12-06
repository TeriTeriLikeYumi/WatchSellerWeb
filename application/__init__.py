from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "0acae532f5ecd418bc9673a246ddfa88a6816114"
app.config["MONGO_URI"] = "mongodb+srv://TeriTeriYumi:<demiwachan2s>@cluster1.iwwrtht.mongodb.net/?retryWrites=true&w=majority"

# setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes