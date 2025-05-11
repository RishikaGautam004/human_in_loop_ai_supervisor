import unittest
import requests

url = "http://localhost:5000/supervisor/respond"
data = { "request_id": "abc123", "answer": "Yes, bridal packages are available." }

response = requests.post(url, json=data)
print(response.json())  # Expected output: {"success": true}
from ai_agent import handle_call

class TestAIAgent(unittest.TestCase):
    def test_known_question(self):
        response = handle_call({"question": "What are your business hours?"})
        self.assertEqual(response["message"], "We are open from 9 AM to 7 PM.")

    def test_unknown_question(self):
        response = handle_call({"question": "Do you offer organic hair treatments?"})
        self.assertTrue(response["request_help"])

if __name__ == '__main__':
    unittest.main()