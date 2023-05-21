#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """flask hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """path added to URL"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """URL path with variable"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """URL path with variable that has default value"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """print n if it is integer"""
    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """html with rule to check odd or even"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, typ='even')
    else:
        return render_template('6-number_odd_or_even.html',
                               number=n, typ='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
