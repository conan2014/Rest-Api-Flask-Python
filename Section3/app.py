# May 28th 2020
from flask import Flask, jsonify, request, render_template

# Create an object of Flask class with a unique name
app = Flask(__name__)

stores = [
    {
        'name': 'store A',
        'items': [
            {
                'name': 'item 1',
                'price': 10.99
            }
        ]
    }
]

# POST - used to receive data and process it
# GET - used to send data back only

@app.route('/')
def home():
    return render_template('index.html')

# POST /store {name:}                                 Receive a store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()  # .get_json() converts JSON string into python dictionary
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>                            Send back a store with a given name
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store                                          Send back a list of stores
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}      Receive an item belonging to a store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item                       Send back a list of items belonging to a store with a given name
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            items = store['items']
            return jsonify({'items': items})
    return jsonify({'message': 'store not found'})

app.run(port=5000)  # run the app