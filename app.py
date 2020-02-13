# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
from flask import request
import random

operations = ['+','-','*','/']

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
def home():
    return render_template("index.html")

# This is the endpoint the button on the front-end calls
# It's purpose is to take a user input and generate a new math question
# This can be expanded to verify that the answer is correct and pull a new question
@app.route('/generate_new_question', methods=['POST'])
def generate_new_question():
    print("The backend has been told to generate a new question.")
    print("The User clicked the button " + str(request.form.get('button_value')))
    opp = operations[random.randint(0,3)]
    val1 = random.randint(100,200)
    val2 = random.randint(50,75)
    return '{"question":"'+ str(val1) +' ' + str(opp) + ' ' + str(val2) + '"}'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
