backend/
│
├── api/
│∝ - __init__. py # API Initialization
│∝ - auth.by # User authentication logic
│└ - orders. py # Order Management Logic
│
∝ - models. py # Database Model Definition
└ -- app. py # Main application file

How to run an application
Create a Python virtual environment and install dependencies:

bash
python -m venv venv
Source venv/bin/activate # Using venv \ Scripts \ activate on Windows
pip install flask flask_sqlalchemy flask_jwt_extended werkzeug
Run Flask application:

bash
python app.py
Conduct API request testing through Postman or Curl, such as registering users, logging in users, creating and viewing orders.
