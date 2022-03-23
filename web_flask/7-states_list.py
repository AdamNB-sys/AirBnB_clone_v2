#!/usr/bin/python3
"""
This script starts a flask web app
listening on 0.0.0.0, port 5000
routes: /: display "Hello HBNB"
with the option strict_slashes=False
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello():
    """uses Flask web app to display 'Hello HBNB!'"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """start the web app as a script"""
    app.run(host="0.0.0.0", port=5000)
