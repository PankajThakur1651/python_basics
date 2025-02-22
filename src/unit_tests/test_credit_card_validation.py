from datetime import *
import credit_card_validation as ccv
import unittest


class TestCreditCardValidation(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("TearDown")

    def test_card_is_not_valid(self):
        with self.assertRaises(RuntimeError):
            ccv.validate_card(date(2022, 12, 12))

    def test_card_is_valid(self):
        is_result = ccv.validate_card(date(2025, 12, 12))
        self.assertEqual(is_result, "Valid")


if __name__ == '__main__':
    unittest.main()
