#!/usr/bin/python3
"""Module to Star a Flask web application for Airbnb_clone,
    and connecting to the database
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_template():
    """Function to return display a template of states from db"""
    states = storage.all(State)
    return render_template('7-states_list.html', States=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the connection to the database"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
