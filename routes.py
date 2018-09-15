from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json
import pickle

app = Flask(__name__)
api = Api(app)

#orders dictionary memory storage
orders = {}

def abort_if_order_doesnt_exist(order_id):
    if order_id not in orders:
        abort(404, message="order {} doesn't exist".format(order_id))

parser = reqparse.RequestParser()
parser.add_argument('orderId')
parser.add_argument('name')
parser.add_argument('price')
parser.add_argument('picture')


# order
# shows a single orderitem and lets you delete an order item
class order(Resource):
    def get(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        return orders[order_id]

    def delete(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        del orders[order_id]
        return '', 204

    def put(self, order_id):
        orderItem = orders[order_id]
        state = {'status':'completed'}
        orderItem.update(state)
        return orderItem

# orderList
# shows a list of all ORDERS, and lets you POST to add new names
class orderList(Resource):
    def get(self):
        return orders

    def post(self):
        args = parser.parse_args()
        orderId = args['orderId']
        name = args['name']
        price = args['price']
        picture = args['picture']
        item = {'orderId':orderId,
                'name':name,
                'price':price,
                'picture':picture,
                'status':'new order'}
        orders[orderId] = item
        return orders, 201


# Api resource routes

api.add_resource(orderList, '/api/v1/users/ORDERS')
api.add_resource(order, '/api/v1/users/ORDERS/<order_id>')


if __name__ == '__main__':
    app.run(debug=True)