import flask, flask.views

class Shows(flask.views.MethodView):
	def get(self):
		return flask.render_template('shows.html')