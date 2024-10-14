
# test_bugfix_1.py

import unittest
from bugfix_1 import calculate_total_price

class TestCalculateTotalPrice(unittest.TestCase):
    
    def test_no_discount(self):
        # 测试没有折扣的情况下总价计算是否正确
        items = [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 3}]
        self.assertEqual(calculate_total_price(items), 350)
    
    def test_with_discount(self):
        # 测试应用折扣的情况下总价计算是否正确
        items = [{'price': 100, 'quantity': 2}, {'price': 50, 'quantity': 3}]
        self.assertEqual(calculate_total_price(items, discount=0.1), 315)
    
    def test_empty_items(self):
        # 测试空订单的情况下总价计算
        items = []
        self.assertEqual(calculate_total_price(items), 0)
    
    def test_discount_0_percent(self):
        # 测试0%折扣情况下总价计算
        items = [{'price': 100, 'quantity': 2}]
        self.assertEqual(calculate_total_price(items, discount=0), 200)
    
    def test_discount_100_percent(self):
        # 测试100%折扣情况下总价为0
        items = [{'price': 100, 'quantity': 2}]
        self.assertEqual(calculate_total_price(items, discount=1), 0)

if __name__ == '__main__':
    unittest.main()
