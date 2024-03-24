#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(_):
    """Close storage."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page."""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
