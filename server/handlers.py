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

class Handler( webapp.RequestHandler ):
	jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
	def render(self, temp, **format_args):
		template = self.jinja_environment.get_template(temp)
		self.response.out.write(template.render(format_args))

	def write_json(self, json_d):
		json_s = json.dumps(json_d)
		self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
		self.response.out.write(json_s)

class Home( Handler ):
	def get(self):
		self.render("templates/home.html")


