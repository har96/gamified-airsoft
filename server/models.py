from google.appengine.ext import ndb
from helpers import *
import json


class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    kills = ndb.IntegerProperty(default=0)
    deaths = ndb.IntegerProperty(default=0)
    performance = ndb.FloatProperty(default=0)
    experience = ndb.IntegerProperty(default=0)

    @classmethod
    def get_by_username(cls, username):
        return cls.query(username=username).fetch(1)
