import unittest

from fast_food_api.routes import app

ORDERDELURL = "/api/v1/users/ORDERS/2"


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_delete_order_item(self):
        response = self.app.delete(ORDERDELURL)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
