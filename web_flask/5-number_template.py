#!/usr/bin/python3
"""
This script starts a Flask web application
The application listens on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Displays python followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display “n is a number” only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
