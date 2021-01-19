#!/usr/bin/python3
""" Module to start a web applicaction and
    display binded messages
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function to return a greeting"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function to return a HBNB at /hbnb url bind"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_message(text):
    """Function to return a message with c"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text):
    """Function to return a message with python"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function to return a number with message"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
