#!/usr/bin/python3
"""DB Storage class"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


Class DBStorage():
    """DBStorage Class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        self.__classes = {"User": User, "Amenity": Amenity, "City": City,
                          "Place": Place, "Review": Review, "State": State}
        self.__class = ["User", "Amenity", "City", "Place", "Review", "State"]
        if getenv('HBNB_ENV') == 'test':
            Base.metadat.drop_all(self.__engine)

    def all(self, cls=None):
        """return objects based value of cls, all objects otherwise"""
        objs = {}
        if cls is None:
            for cl in self.__class:
                ls_cl = session.query(cl).all()
                if ls_cl:
                    for c in ls_cl:
                        objs[c.__class__.name + '.' + c.id] = c
        else:
            ls_cl = session.query(cls).all()
            if ls_cl:
                for c in ls_cl:
                    objs[c.__class__.name + '.' + c.id] = c
        return objs

    def new(self):
        """add object to current session"""
        self.__session.add(self)

    def save(self):
        """commit all changes in current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from current session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creating session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))
