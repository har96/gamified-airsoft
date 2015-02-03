from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import images
import jinja2
from models import *
from helpers import *
import logging
import os
import time
import json

SUCCESS = {"success":True}

class Handler( webapp.RequestHandler ):
	jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
	def render(self, temp, **format_args):
		template = self.jinja_environment.get_template(temp)
		self.response.out.write(template.render(format_args))

	def write_json(self, json_d):
		json_s = json.dumps(json_d)
		self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
		self.response.out.write(json_s)

class AddUser( Handler ):

    def post(self):
       username = self.request.get("username")
           
       user = User(username=username)
       user.put()

       self.write_json(SUCCESS)


class GetUser( Handler ):

    def get(self, username):

        user = User.get_by_username(username)

        info = {"performance": user.performance,
                "experience": user.experience,
                "deaths":user.deaths,
                "kills":user.kills}

        self.write_json(info)


class RegisterDeath( Handler ):

    def post(self):
        death = self.request.get("death")
        kill = self.request.get("kill")

        killer = User.get_by_username(kill)
        killer.kills += 1
        killer.put()

        user = User.get_by_username(death)
        user.deaths += 1
        user.put()

        self.write_json(SUCCESS)
