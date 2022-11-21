from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixIn

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretekey'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(80), nullable = False)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
