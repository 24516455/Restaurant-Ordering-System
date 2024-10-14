# app/routes.py

from flask import render_template, request, redirect, url_for
from . import db
from .models import MenuItem, Order
from flask import current_app as app

@app.route('/')
def index():
    menu_items = MenuItem.query.all()
    return render_template('index.html', menu_items=menu_items)

@app.route('/order', methods=['POST'])
def order():
    total_price = 0
    selected_items = request.form.getlist('items')
    order_items = []

    for item_id in selected_items:
        item = MenuItem.query.get(item_id)
        if item:
            order_items.append(item)
            total_price += item.price

    new_order = Order(total_price=total_price)
    db.session.add(new_order)
    db.session.commit()

    return redirect(url_for('index'))

