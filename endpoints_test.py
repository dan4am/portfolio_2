import unittest
import schemas
from main import app
from fastapi.testclient import TestClient

client = TestClient()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
