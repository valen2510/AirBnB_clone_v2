#!/usr/bin/python3
"""Module to start a web applicaction and
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
    """Function to return a greeting"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
