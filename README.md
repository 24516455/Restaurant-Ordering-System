

#Order History Function Module

This module is responsible for displaying the user's order history. Users can view all previous order details, including order ID and total price.

catalogue

-[Function] (# Function)
-[Instructions] (# Instructions)
-[File Structure] (# File Structure)
-[Dependency] (# Dependency)
-[Contribution Guide] (# Contribution Guide)

##Function

-* * View historical orders * *: Users can access the order history page to view all their historical order records.

##Instructions for use

###Installation and configuration

1. * * Ensure the main application * *: This module needs to run in the Flask application. Please ensure that your main application is installed and running correctly.

2. * * Import Module * *: Register the blueprint of this functional module in the ` __init__. py ` file of the main application.

```python
from features.order_history import order_history_bp

app.register_blueprint(order_history_bp)
```

3. * * Configure database * *: Ensure that there is order data in the database. You can use the provided example orders or add them according to the application logic.

###Routing

The routes added to this module include:

-GET/order_ristory: Returns the user's order history page.

###Use

Users only need to access` http://127.0.0.1:5000/order_history `You can view your order history. The page will display a list of all orders.

##File Structure

```
features/
└── order_history/
∝ -- __init__. py # Module initialization
∝ - routes. py # Route Definition
└── templates/
└ - order_cistory.html # Order History Page Template
```

##Dependency

This module relies on Flask and Flask QLAlchemy in the main application. Ensure that these libraries are installed in your main application:

```bash
pip install Flask Flask-SQLAlchemy
```

##Contribution Guide

Welcome to contribute! If you have any improvements or suggestions for this module, please follow the steps below:

1. Fork the project
2. Create your feature branch (` git checkout - b features/my features `)
3. Submit changes (` git commit am 'Add some features' `)
4. Push to branch (` git push origin feature/my feature `)
5. Create a Pull Request

