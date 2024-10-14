
#Features/Order History/Initialization. py

Import blueprint from flask

Order_cistory_bp=blueprint ("order_cistory", __name__)

From. Import Route # Import Route

#Features/Order History/Route. py

Import render_template from Flask
From. Import Orders_History_ bp
Import orders from app. models

@order_history_bp.route（'/order_history'）
Define order history ():
Orders=Order. query. all() # Query all orders
Return render_template ('order_cistory. html ', orders=orders)

<!--  Features/Order History/Templates/Order History. html ->

<! DOCTYPE html>
<html lang=“en”>
<head>
<meta character set="UTF-8">
<meta name="viewport" content="width=device width, initial - s
#Features/Order History/Initialization. py

Import blueprint from flask

Order_cistory_bp=blueprint ("order_cistory", __name__)

From. Import Route # Import Route

#Features/Order History/Route. py

Import Rendering from Flask - Template
From. Import Orders_History_ bp
Import documents from app. models

@order_history_bp.route（'/order_history'）
Define order history ():
Orders=Order. query. all() # Query all orders
Return render_template ('order_cistory. html ', orders=orders)

<!--  Features/Order History/Templates/Order History. html ->

<! DOCTYPE html>
<html lang=“en”>
<head>
<meta character set="UTF-8">
<meta name="viewport" content="width"=device width, initial scale=1.0 ">
<title>Catalog History</title>
<Link rel="Style Sheet" ref="{url_for 'Static', file name='ss/style. css')}">
</head>
<body>
<h1>Your order history</h1>
<ul>
{% represents the order% in the order%}
<li>Order ID: {order. ID}}, Total Price: ¥ {order. total price}}</li>
%endfor%
</ul>
</body>
</html>
le=1.0“>
<title>Catalog History</title>
<link rel="stylesheet" ref="{url_for ('static ', file name=' ss/style. css')}">
</head>
<body>
<h1>Your order history</h1>
<ul>
{% represents the order% in the order%}
<li>Order ID: {order. ID}}, Total Price: ¥ {order. total price}}</li>
｛%endfor%｝
</ul>
</body>
</html>
