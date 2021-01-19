#!/usr/bin/python3
"""Module to display the states and the cities in a template
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_template():
    """Function to return display a template of cities from db"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the connection to the database"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
