import unittest # testing library
# current app
from flask import current_app
# model
from app import db, User, Task
from app import create_app

class FirstTestCase(unittest.TestCase):
    # before test
    def setUp(self):
        pass
    # after test
    def tearDown(self):
        pass

    def test_first(self):
        self.assertTrue(1 == 1)
