# backend/api/orders.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Order

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
@jwt_required()
def create_order():
data = request.get_json()
item_name = data.get('item_name')
quantity = data.get('quantity')

if not item_name or not quantity:
return jsonify({"msg": "Missing item_name or quantity"}), 400

#Get the current user's ID
user_id = get_jwt_identity()

#Create an order
new_order = Order(item_name=item_name,  quantity=quantity, user_id=user_id)
db.session.add(new_order)
db.session.commit()

return jsonify({"msg": "Order created successfully"}), 201

@orders_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_orders():
user_id = get_jwt_identity()
orders = Order.query.filter_by(user_id=user_id).all()

result = [{"id": order.id, "item_name": order.item_name, "quantity": order.quantity} for order in orders]

return jsonify(result), 200

@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order(order_id):
user_id = get_jwt_identity()
order = Order.query.filter_by(id=order_id, user_id=user_id).first()

if not order:
return jsonify({"msg": "Order not found"}), 404

db.session.delete(order)
db.session.commit()

return jsonify({"msg": "Order deleted successfully"}), 200
