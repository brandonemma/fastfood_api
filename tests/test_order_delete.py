import json
import unittest

from app.views import app
ORDERDELURL = "/api/v1/users/ORDERS/2"


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_delete_order_item(self):
        response = self.app.delete(ORDERDELURL)
        response_data = 'order item deleted'
        data = json.loads(response.data)
        #self.assertEqual(response.status_code, 204)
        self.assertEqual(data['message'],response_data)

if __name__ == "__main__":
    unittest.main()
