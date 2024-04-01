import os, sys
from pathlib import Path
test_path = os.path.dirname(__file__)
src_path =os.path.dirname(test_path)
src_path=os.path.join(src_path, "src")
sys.path.append(src_path)

import unittest
from employee import Employee
from unittest.mock import patch

class Test_Employee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp_pankaj=Employee('pankaj' ,'thakur', 80000)
        self.emp_yashvi=Employee('yashvi','thakur', 800000)
        return super().setUp()
    
    @classmethod
    def setUpClass(cls) -> None:
        print("Setup class ")
        return super().setUpClass()
    @classmethod
    def tearDownClass(cls) -> None:
        print("Tear Down class ")
        return super().tearDownClass()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_email(self):
        self.assertEqual(self.emp_pankaj.email, 'pankaj.thakur@gmail.com')
        self.assertEqual(self.emp_yashvi.email, 'yashvi.thakur@gmail.com')
    
    def test_name(self):
        self.assertEqual(self.emp_pankaj.fullname, 'pankaj thakur')
        self.assertEqual(self.emp_yashvi.fullname, 'yashvi thakur')
        
    def test_apply_raise(self):
        self.assertEqual(self.emp_pankaj.apply_raise(), 84000)
        self.assertEqual(self.emp_yashvi.apply_raise(), 840000)
    
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='success'
            schedule =self.emp_pankaj.monthly_schedule('March')
            mocked_get.assert_called_with('https://company.com/thakur/March')
            self.assertEqual(schedule, 'success')
            
            

if __name__ =='__main__':
    unittest.main()