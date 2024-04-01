import os, sys
from pathlib import Path
test_path = os.path.dirname(__file__)
src_path =os.path.dirname(test_path)
src_path=os.path.join(src_path, "src")
sys.path.append(src_path)

import calc 
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        result= calc.add(10,5)
        self.assertEqual(result, 15)
        
    def test_multiply(self):
        result= calc.multiply(10,5)
        self.assertEqual(result, 50)
    
    def test_divide(self):
        self.assertEqual(calc.divide(5,2), 2.5)
        self.assertRaises(ValueError, calc.divide, 5, 0)
        # second Method to catch exception
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
            
if __name__ =='__main__':
    unittest.main()