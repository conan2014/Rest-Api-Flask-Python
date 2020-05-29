# May 29th 2020
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)   # allow us to easily add resources to the flask app

# define a Student resource
class Student(Resource):
    def get(self, name):   # define the method the Student resource gonna accept
        return {'student': name}  # define what the method is gonna do when the endpoint is called

api.add_resource(Student, '/student/<string:name>')  # tell the api object that the Student resource
                                                     # we created above will be accessible via the api
                                                     # so the decorator @app.route('/student/<string:name>') is no longer needed

app.run(debug=True, port=5000)









