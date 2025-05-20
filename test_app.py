import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # sends HTTP GET request to the application
        result = self.app.get('/')
        # assert the status code and response data
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello from GitHub Actions + SonarQube + Docker!")

if __name__ == '__main__':
    unittest.main()
