# backend/database.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create SQLAlchemy object
db = SQLAlchemy()

def init_app(app: Flask):
"""
Initialize Flask application and database.

: param app: Flask application instance
"""
app.config['SQLALCHEMY_DATABASE_URI'] = ' sqlite:///app.db # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
App. secret_key='superecretkey '# You should use a more secure key
Db. init_mapp (app) # Bind db objects to Flask application instances

class User(db. Model):
"" "User Model" ""
id = db.Column(db. Integer, primary_key=True)
username = db.Column(db. String(80),  unique=True, nullable=False)
password = db.Column(db. String(120), nullable=False)

class Order(db. Model):
Order Model
id = db.Column(db. Integer, primary_key=True)
item_name = db.Column(db. String(120), nullable=False)
quantity = db.Column(db. Integer, nullable=False)
user_id = db.Column(db. Integer, db.ForeignKey('user.id'), nullable=False)
user = db.relationship('User', backref=db.backref('orders', lazy=True))


