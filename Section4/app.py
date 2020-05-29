# May 29th 2020

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)   # create an Api object so that we can add resources to it

class Student(Resource):   # define a Student resource
    def get(self, name):   # define a get method the Student resource is gonna accept
        return {'student': name}  # define what the method is gonna do when the endpoint is called

api.add_resource(Student, '/student/<string:name>')  # add Student resource to the api, so that the resource can be accessed via the api
                                                     # so the decorator @app.route('/student/<string:name>', methods=['GET']) is no longer needed

app.run(debug=True, port=5000)

