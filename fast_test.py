import unittest
from flask import request, jsonify, json
from routes import app


ALLORD_URL = "http://localhost:5000/api/v1/users/ORDERS"
POST_URL = "http://localhost:5000/api/v1/users/ORDERS"
PUT_URL = "http://localhost:5000/api/v1/users/ORDERS/1"
FETCH_URL = "http://localhost:5000/api/v1/users/ORDERS/1"


class Test(unittest.TestCase):

    def test_get_all(self):
    	response = self.app.get(ALLORD_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200) 

if __name__ =="__main__":
	unittest.main()
