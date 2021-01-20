#!/usr/bin/python3
"""Module to display the states and the cities in a template
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_template():
    """Function to return display a template of states from db"""
    states = storage.all(State)
    return render_template('7-states_list.html', States=states.values())


@app.route('/states/<id>', strict_slashes=False)
def city_id_template(id):
    """Function to return display a template of cities from state id from db"""
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html', state=state, id=id)
    return render_template('9-states.html', state=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Function to close the connection to the database"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
