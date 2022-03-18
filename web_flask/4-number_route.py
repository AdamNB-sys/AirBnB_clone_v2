#!/usr/bin/python3
#########################################
# This script starts a flask web app    #
# listening on 0.0.0.0, port 5000       #
# routes: /: display "Hello HBNB"       #
# with the option strict_slashes=False  #
#########################################
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """uses Flask web app to display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """uses Flask web app to display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isnt_fun(text):
    """
    Uses Flask web app to display 'C'
    followed by the value of the text variable
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def route_python(text='is cool'):
    """
    Uses Flask web app to display 'Python'
    followed by the value of the text variable
    """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def route_number(n):
    """uses Flask web app to display a number"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    """start the web app as a script"""
    app.run(host="0.0.0.0", port=5000)
