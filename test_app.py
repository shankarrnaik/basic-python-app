# test_app.py
import unittest
from app import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
