#!/usr/bin/python3
"""print states based on id or not"""
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


@app.route('/states/')
@app.route('/states/<id_s>')
def cities_by_states(id_s="all"):
    states = storage.all("State")
    if id_s == "all":
        return render_template("9-states.html", state="all",
                               name="States",
                               states=states.values())
    else:
        flag = False
        state = None
        for k, v in states.items():
            if k == id_s:
                flag = True
                state = v
                break
        if flag:
            result = state.cities
            return render_template("9-states.html", state="1",
                                   name="State: {}".format(state.name),
                                   states=result)
        else:
            return render_template("9-states.html", state="",
                                   name="Not found!",
                                   states=states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
