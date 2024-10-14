# app/__init__.py

#Version number of the package
__version__ = '1.0.0'

#Import main modules
From. routes import app as application # Assuming that a Flask application instance is defined in routes. py
From. models import db # Assuming database instances are defined in models.py

#Initialize some core components
def create_app():
Create and configure Flask applications
application.config.from_object('config.  Config '# Import Configuration
Db. init_mapp (application) # Initialize database

with application.app_context():
From. import routes # Import routes
Db. create_all() # Create a database table (if it does not exist)

return application

#Additional initialization code may need to be added, such as:
#- Configure logs
#- Registration blueprint
#- Configure CORS, etc

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from features.order_history import order_history_bp
from features.promotions import promotions_bp
from features.user_account import user_account_bp

db = SQLAlchemy()

def create_app():
app = Flask(__name__)
app.config.from_object('config. Config')
    
db.init_app(app)

#Registration blueprint
app.register_blueprint(order_history_bp)
app.register_blueprint(promotions_bp)
app.register_blueprint(user_account_bp)

with app.app_context():
db.create_all()

return app
