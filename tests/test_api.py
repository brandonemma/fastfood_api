import json
import unittest


from app.views import app
from app.models import *

ORDERSLISTURL = "/api/v1/users/ORDERS"
ORDERURL = "/api/v1/users/ORDERS/1"
ORDERURL2 = "/api/v1/users/ORDERS/2"
ORDERDELURL = "/api/v1/users/ORDERS/2"


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_get_order_list(self):
        response = self.app.get(ORDERSLISTURL)
        self.assertEqual(response.status_code, 200)

    def test_get_order_item_status(self):
        response = self.app.get(ORDERURL)
        self.assertEqual(response.status_code, 200)

    def test_get_order_item_1_data(self):
        response = self.app.get(ORDERURL)
        data = json.loads(response.data)
        # create order schema
        order_schema = OrderSchema()
        # order object
        order = Order('1', 'oranges', 500, 'new order')
        # serialise order object
        result = order_schema.dump(order)
        # check whether the response data from request is equal to the serialised data
        self.assertEqual(data, result.data)

    def test_get_order_item_2_data(self):
        response = self.app.get(ORDERURL2)
        data = json.loads(response.data)
        order_schema = OrderSchema()
        # obj = order_schema.load(data)
        order = Order('2', 'peaches', 600, 'new order')

        result = order_schema.dump(order)

        self.assertEqual(data, result.data)

    def test_get_order_item_list(self):
        response = self.app.get(ORDERSLISTURL)
        data = json.loads(response.data)
        # created objects
        order = Order('1', 'oranges', 500, 'new order')
        order1 = Order('2', 'peaches', 600, 'new order')
        # add objects to collection list
        orderCollection = [order, order1]
        # create schema for serialising collection of objects
        ordersSchema = OrderSchema(many=True)
        # serialise list of order objects
        results = ordersSchema.dump(orderCollection)
        self.assertEqual(data, results.data)

  
        

    def test_post_order_item_data_response(self):
        item = {'orderId': "3",
                'name': "bananas",
                'price': 750,
                'status': 'new order'}
                
        response_data = 'order item added'
        response = self.app.post(ORDERSLISTURL, data=item)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'],response_data)



    def test_put_order_item(self):
        state = {'status': 'completed'}
        response = self.app.put(ORDERURL, data=state)
        self.assertEqual(response.status_code, 200)
 

if __name__ == "__main__":
    unittest.main()
