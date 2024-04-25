#!/usr/bin/python3
"""Script that starts a Flask web application:
The web application must be listening on 0.0.0.0, port 5000
Must use storage for fetching data from the storage engine.
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
"""
from flask import Flask
from flask import storage
from flask import render_template

app = Flask(__name__)


@app.route("/state_list", strict_slashes=False)
def strict_list():
    """Display a HTML page inside the tag BODY with the list
    of all State objects present in DBStorage sorted by name
    """
    return render_templates("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
