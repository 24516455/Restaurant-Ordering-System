# test_bugfix_2.py

import unittest
from flask import session
from bugfix_2 import app

class TestUserAccount(unittest. TestCase):
    
def setUp(self):
#Set up test client
self.app = app.test_client()
self.app.testing = True

def test_account_page_without_login(self):
#When accessing the account page without logging in, you should be prompted to log in
response = self.app.get('/account')
self.assertEqual(response.status_code, 200)
Self. insertIn (b 'Please log in to view your account information', response. data)

def test_account_page_with_login(self):
#Simulate user login and access to account page
with self.app.session_transaction() as sess:
sess['user_id'] = 1
sess['user_name'] = 'Alice'
        
response = self.app.get('/account')
self.assertEqual(response.status_code, 200)
Self. insertIn (b 'Welcome, Alice', response.data)

def test_login(self):
#Test whether the login page returns normally
response = self.app.get('/login')
self.assertEqual(response.status_code, 200)

def test_logout(self):
#Test whether the user session is cleared after logging out
with self.app.session_transaction() as sess:
sess['user_id'] = 1
sess['user_name'] = 'Alice'
        
response = self.app.get('/logout',  follow_redirects=True)
self.assertEqual(response.status_code, 200)
self.assertNotIn('user_id', session)
self.assertNotIn('user_name', session)

if __name__ == '__main__':
unittest.main()
