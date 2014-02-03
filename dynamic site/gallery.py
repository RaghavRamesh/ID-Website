import flask, flask.views

class Gallery(flask.views.MethodView):
	def get(self):
		return flask.render_template('gallery.html')