import unittest
import requests

url = "http://localhost:5000/request_help"
data = { "question": "Do you offer bridal packages?" }

response = requests.post(url, json=data)
print(response.json())  # Expected output: {"request_id": "some_id"}

from supervisor_handler import create_help_request

class TestSupervisorHandler(unittest.TestCase):
    def test_create_request(self):
        request_id = create_help_request({"question": "Do you have VIP rooms?"})
        self.assertIsNotNone(request_id)

if __name__ == '__main__':
    unittest.main()