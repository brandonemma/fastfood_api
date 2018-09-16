from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello():
    return "Hello World!"


# orders dictionary memory storage
orders = {
    "1":
        {'orderId': 1,
         'name': 'oranges',
         'price': 500,
         'picture': 'oranges.jpg',
         'status': 'new order'},
    "2":
        {'orderId': 2,
         'name': 'peaches',
         'price': 600,
         'picture': 'peaches.jpg',
         'status': 'new order'}
}


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
        pass

    def delete(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        del orders[order_id]
        return '', 204
        pass

    def put(self, order_id):
        order_item = orders[order_id]
        state = {'status': 'completed'}
        order_item.update(state)
        return order_item, 200
        pass


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
        item = {'orderId': orderId,
                'name': name,
                'price': price,
                'picture': picture,
                'status': 'new order'}
        orders[orderId] = item
        return orders, 201


# Api resource routes

api.add_resource(orderList, '/api/v1/users/ORDERS')
api.add_resource(order, '/api/v1/users/ORDERS/<order_id>')

if __name__ == '__main__':
    app.run(debug=True)
