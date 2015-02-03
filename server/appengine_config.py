from google.appengine.ext.appstats import recording

def webapp_add_wsgi_middleware(app):
	# apply appstats middleware
	app = recording.appstats_wsgi_middleware(app)
	return app
