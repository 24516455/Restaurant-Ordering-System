# backend/api/auth.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app import db
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
data = request.get_json()
username = data.get('username')
password = data.get('password')
    
if not username or not password:
return jsonify({"msg": "Missing username or password"}), 400

#Check if the username already exists
if User.query.filter_by(username=username).first():
return jsonify({"msg": "Username already exists"}), 400
    
#Create a new user
hashed_password = generate_password_hash(password)
new_user = User(username=username,  password=hashed_password)
db.session.add(new_user)
db.session.commit()

return jsonify({"msg": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
data = request.get_json()
username = data.get('username')
password = data.get('password')

#Search for Users
user = User.query.filter_by(username=username).first()
if not user or not check_password_hash(user.password, password):
return jsonify({"msg": "Invalid username or password"}), 401

#Create JWT access token
access_token = create_access_token(identity=user.id)
return jsonify(access_token=access_token), 200
