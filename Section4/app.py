# May 29th 2020

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'conan'  # this key has to be secure and secret, only you should know, make this long, random, and secret in a real app
api = Api(app)   # create an Api object so that we can add resources to it

jwt = JWT(app, authenticate, identity)  # when we initialize a jwt object, this is gonna utilize the app object, authenticate & identity methods
                                        # to allow for authentication of users
                                        # As soon as we initialize a jwt object, Flask-JWT registers an endpoint with our application, /auth

items = [
    {
        "name": 'chair',
        "price": 10.99
    }
]

class Item(Resource):
    @jwt_required()   # @jwt_required() ensures that a user needs to get authenticated before accessing the get() method
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
        parser = reqparse.RequestParser() # initialize a new object that we can use to parse the JSON payload (not to be confused with JWT payload)
        parser.add_argument('price',
                            type=float,
                            required=True,
                            help="This field cannot be left blank!")
        data = parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item.update(data)
        else:
            item = {"name": name, "price": data['price']}
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

