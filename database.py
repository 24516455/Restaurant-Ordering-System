# backend/database.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建 SQLAlchemy 对象
db = SQLAlchemy()

def init_app(app: Flask):
    """
    初始化 Flask 应用与数据库。

    :param app: Flask 应用实例
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # SQLite 数据库
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'supersecretkey'  # 你应该使用更安全的密钥
    db.init_app(app)  # 将 db 对象与 Flask 应用实例绑定

class User(db.Model):
    """用户模型"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Order(db.Model):
    """订单模型"""
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))


