from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def dashboard():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = {
            "username":username,
            "password":password
        }
        return jsonify(user),200