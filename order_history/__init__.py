
# features/order_history/__init__.py

from flask import Blueprint

order_history_bp = Blueprint('order_history', __name__)

from . import routes  # 导入路由

# features/order_history/routes.py

from flask import render_template
from . import order_history_bp
from app.models import Order

@order_history_bp.route('/order_history')
def order_history():
    orders = Order.query.all()  # 查询所有订单
    return render_template('order_history.html', orders=orders)

<!-- features/order_history/templates/order_history.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>订单历史</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>您的订单历史</h1>
    <ul>
        {% for order in orders %}
        <li>订单ID: {{ order.id }}, 总价: ¥{{ order.total_price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
