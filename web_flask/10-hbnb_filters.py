#!/usr/bin/python3
"""
display html page
"""
from models import storage
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb_filters/')
def hbnb_filters():
    states = storage.all("State").values()
    result = []
    for state in sorted(states, key=lambda x: x.name):
        result.append([state, state.cities])
    amenities = storage.all("Amenity").values()
    return render_template("10-hbnb_filters.html",
                           amenities=amenities, result=result)


@app.teardown_appcontext
def close_session(exception):
    """remove the session to see what happened"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
