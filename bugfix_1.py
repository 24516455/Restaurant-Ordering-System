




def calculate_total_price(items, discount=0):
"""
Calculate the total price of the order and apply discounts.
    
: param items: a list of items in the order, each item is a dictionary containing "price" and "quantity" keys.
: param discount: discount ratio, for example, 0.1 represents a 10% discount.
Return: The total price after applying the discount.
"""
total_price = 0
for item in items:
total_price += item['price'] * item['quantity']

#Fix: Apply discounts
if discount > 0:
total_price = total_price * (1 - discount)

return total_price

#Example data
order_items = [
{'price ': 100,' quantity ': 2}, # commodity 1, total price 200
{'price ': 50,' quantity ': 3}, # commodity 2, total price 150
]

#Discount not applied before repair
Print ("pre fix:", calculate_total_price (order_items)) # No discount applied

#Discount application after repair
Print ("fixed:", calculate_total_price (order_items, discount=0.1)) # Apply 10% discount
