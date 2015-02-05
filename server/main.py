from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from handlers import *

app = webapp.WSGIApplication([
    ("/newuser", AddUser),
    ("/user/([a-zA-Z]+)", GetUser),
    ("/death", RegisterDeath)], debug=True)
