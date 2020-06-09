# May 29th 2020

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)   # create an Api object so that we can add resources to it

items = [
    {
        "name": 'chair',
        "price": 10.99
    }
]

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) # filter() returns a filter object, next() gives us the first item found in the filter iterator
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        request_data = request.get_json()  # get JSON payload and convert it to Python dictionary
        new_item = {
            "name": name,
            "price": request_data['price']
        }
        items.append(new_item)
        return new_item, 201

    def put(self, name):   # put is idempotent, which means no matter how many times you call it, the output never changes
                           # so if you call put 10 times, you won't create 10 new items, you only create 1 item
        request_data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item.update(request_data)
        else:
            item = {"name": name, "price": request_data['price']}
            items.append(item)
        return item, 200

    def delete(self, name):
        global items  # call global variable items here so that python won't throw an error saying we're using items to define the variable below called 'items'
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')  # endpoint /item/<string:name> can be accessed via the api object
api.add_resource(ItemList, '/items')

app.run(debug=True, port=5000)

