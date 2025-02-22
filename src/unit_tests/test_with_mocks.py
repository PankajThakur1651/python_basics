from unittest.mock import MagicMock
from unittest.mock import Mock
import unittest
class Service:
    def get_data(self):
        return "Real Data"

class TestService(unittest.TestCase):
    def test_mock_service(self):
        service = Service()
        service.get_data = MagicMock(return_value="Mocked Data")
        print(service.get_data())
        self.assertEqual(service.get_data(), "Mocked Data")



class TestServiceAgain(unittest.TestCase):
    def test_create_basic_mock(self):
        # Create a mock object
        fake_api= Mock()
        # Define behavior for the mock
        fake_api.get_data.return_value={"id": 1, "name": "Mocked Api"}

        # Use the mock
        response = fake_api.get_data()
        print(response)


    def test_mocking_method_with_side_effects(self):
        fake_api=Mock()
        fake_api.get_data.side_effect = ValueError("API is down!")

        try:
            fake_api.get_data()
        except ValueError as e:
            print(e)  # Output: API is down!

        fake_api.get_data.side_effect = [{"id": 1}, {"id": 2}, {"id": 3}]

        print(fake_api.get_data())  # Output: {'id': 1}
        print(fake_api.get_data())  # Output: {'id': 2}
        print(fake_api.get_data())  # Output: {'id': 3}

        def custom_function():
            return {"message": "Hello from the function"}

        fake_api.get_data.side_effect = custom_function
        print(fake_api.get_data())  # Output: {'message': 'Hello from the function'}

        fake_api.get_data()
        assert fake_api.get_data.called  # True

        fake_api.get_data()
        fake_api.get_data()
        self.assertEqual(fake_api.get_data.call_count,8)  # Output: 8



