# test_bugfix_1.py

import unittest
from bugfix_1 import calculate_total_price

class TestCalculateTotalPrice(unittest. TestCase):
    
def test_no_discount(self):
#Test whether the total price calculation is correct without discounts
items = [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 3}]
self.assertEqual(calculate_total_price(items), 350)
    
def test_with_discount(self):
#Test whether the total price calculation is correct when applying discounts
items = [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 3}]
self.assertEqual(calculate_total_price(items, discount=0.1), 315)
    
def test_empty_items(self):
#Total price calculation when testing empty orders
items = []
self.assertEqual(calculate_total_price(items), 0)
    
def test_discount_0_percent(self):
#Total price calculation under 0% discount test
items = [{'price': 100, 'quantity': 2}]
self.assertEqual(calculate_total_price(items, discount=0), 200)
    
def test_discount_100_percent(self):
#The total price is 0 under 100% discount testing
items = [{'price': 100, 'quantity': 2}]
self.assertEqual(calculate_total_price(items, discount=1), 0)

if __name__ == '__main__':
unittest.main()
