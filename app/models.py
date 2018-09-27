from flask_marshmallow import Schema

#order class for representing order model
class Order(object):
    def __init__(self, order_id, name, price, picture, status):
        self.orderId = order_id
        self.name = name
        self.price = price
        self.picture = picture
        self.status = status

    def get_order_id(self):
        return self.orderId

    def set_status(self, state):
        self.status = state

#representation of the object
    def __repr__(self):
        return 'Order Item: {}'.format(self.name)

#schema for the model required for serialising and desirialising modal class
class OrderSchema(Schema):
    class Meta:
        fields = ('orderId',
                  'name',
                  'price',
                  'picture',
                  'status')
