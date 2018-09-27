from flask import Flask, jsonify, Response
import json

from flask_restful import reqparse, abort, Api, Resource

from .models import *

app = Flask(__name__)
api = Api(app)

#persistent data objects
order = Order('1', 'oranges', 500, 'new order')
order1 = Order('2', 'peaches', 600, 'new order')

#create a collection list for the persistent objects
orderCollection = [order, order1]

#create schema objects for oderobjects and order object collections
orderSchema = OrderSchema()
ordersSchema = OrderSchema(many=True)

#serialise order objects and order collection
result = orderSchema.dump(order)
results = ordersSchema.dump(orderCollection)


@app.route("/")
def hello():
    return jsonify(results.data)



def abort_if_order_doesnt_exist(order_id):
    if order_id not in orderCollection:
        abort(404, message="order {} doesn't exist".format(order_id))

#getting the post form data
parser = reqparse.RequestParser()
parser.add_argument('orderId')
parser.add_argument('name')
parser.add_argument('price')



#endpoints for showing ,deleting and updating single order item in the collection

class order(Resource):
    def get(self, order_id):
        o = self.find_order(order_id)
        if o:
            result_data = orderSchema.dump(o)
            return jsonify(result_data.data)
        else:
            pass
        abort(404, message="order {} doesn't exist".format(order_id))

    def delete(self, order_id):
        # abort_if_order_doesnt_exist(order_id)
        o = self.find_order(order_id)
        # del orders[order_id]
        orderCollection.remove(o)

        if len(orderCollection) == 2:
            return {'message':'order item deleted'}
        else:
            return {'message':'delete failed'}
       


    def put(self, order_id):
        o = self.find_order(order_id)
        o.set_status('completed')
        update_result = orderSchema.dump(o)
        return jsonify(update_result.data)

    def find_order(self, order_id):
        f_order = ''
        for order_item in orderCollection:
            if order_item.get_order_id() == order_id:
                f_order = order_item
                break
        return f_order


#endpoint for adding an order item to the collection and showing all order items in the collection
class orderList(Resource):
    def get(self):
        return jsonify(results.data)

    def post(self):
        args = parser.parse_args()

        orderId = args['orderId']
        name = args['name']
        price = args['price']
        

        order_item = Order(orderId, name, price, 'new order')

        orderCollection.append(order_item)
        #ordersSchema = OrderSchema(many=True)
        #results = ordersSchema.dump(orderCollection)
        if len(orderCollection) == 3:
            return {'message':'order item added'}
        else:
            return {'message':len(orderCollection) }
         
        


# Api resource routes

api.add_resource(orderList, '/api/v1/users/ORDERS')
api.add_resource(order, '/api/v1/users/ORDERS/<order_id>')
