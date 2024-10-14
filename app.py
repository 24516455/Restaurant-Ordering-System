
# backend/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ' sqlite:///app.db '
App. config ['JW_SECRET_KEY ']='superscentkey' # You should use a more secure key

db = SQLAlchemy(app)
jwt = JWTManager(app)

from api.auth import auth_bp
from api.orders import orders_bp

#Register API Blueprint
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')

if __name__ == '__main__':
with app.app_context():
Db. create_all() # Initialize database
app.run(debug=True)

# backend/app.py

from flask import Flask
from database import init_app, db
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# 初始化数据库
init_app(app)

jwt = JWTManager(app)

from api.auth import auth_bp
from api.orders import orders_bp

# 注册 API 蓝图
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 初始化数据库
    app.run(debug=True)

# backend/app.py

from flask import Flask
from database import init_app, db
from flask_jwt_extended import JWTManager

app = Flask(__name__)

#Initialize database
init_app(app)

jwt = JWTManager(app)

from api.auth import auth_bp
from api.orders import orders_bp

#Register API Blueprint
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(orders_bp, url_prefix='/api')

if __name__ == '__main__':
with app.app_context():
Db. create_all() # Initialize database
app.run(debug=True)
