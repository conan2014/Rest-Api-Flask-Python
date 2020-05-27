from flask import Flask

# Create an object of Flask class with a unique name
app = Flask(__name__)

# Create a route which was for the home page of our application
@app.route('/') # '/' is the end point, '/' means the home page
def home(): # assign a method to it, whatever the method returns goes to the browser
    return 'Hello, world!'

app.run(port=5000)  # run the app