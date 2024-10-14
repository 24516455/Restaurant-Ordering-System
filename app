# app/config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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

<!-- app/templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>餐厅点单</title>
</head>
<body>
    <h1>菜单</h1>
    <form action="{{ url_for('order') }}" method="POST">
        <ul>
            {% for item in menu_items %}
            <li>
                <input type="checkbox" name="items" value="{{ item.id }}"> {{ item.name }} - ¥{{ item.price }}
            </li>
            {% endfor %}
        </ul>
        <button type="submit">提交订单</button>
    </form>
</body>
</html>
