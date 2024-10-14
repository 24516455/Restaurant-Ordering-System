# app/models.py

from . import db

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    menu_items = db.relationship('MenuItem', backref='order', lazy=True)
    total_price = db.Column(db.Float, nullable=False)

