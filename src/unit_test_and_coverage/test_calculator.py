# test_calculator.py

import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

if __name__ == "__main__":
    unittest.main()

'''
1. Write main code
2. Write test code for main file
3. python3 -m coverage run test_calculator.py
4. python3 -m coverage report

'''