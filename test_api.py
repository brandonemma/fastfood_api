import unittest
from routes import app

ORDERSLISTURL = "/api/v1/users/ORDERS"
ORDERURL = "/api/v1/users/ORDERS/1"
ORDERDELURL = "/api/v1/users/ORDERS/2"


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        pass

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_get_order_list(self):
        response = self.app.get(ORDERSLISTURL)
        self.assertEqual(response.status_code, 200)

    def test_get_order_item(self):
        response = self.app.get(ORDERURL)
        self.assertEqual(response.status_code, 200)

    def test_post_order_item(self):
        item = {'orderId': "2",
                'name': "bananas",
                'price': 750,
                'picture': "bananas.jpg",
                'status': 'new order'}

        response = self.app.post(ORDERSLISTURL, item)
        self.assertEqual(response.status_code, 201)

    def test_put_order_item(self):
        state = {'status': 'completed'}
        response = self.app.put(ORDERURL, state)
        self.assertEqual(response.status_code, 200)

    def test_delete_order_item(self):
        response = self.app.delete(ORDERDELURL)
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()
