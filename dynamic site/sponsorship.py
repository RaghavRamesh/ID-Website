import flask, flask.views

class Sponsorship(flask.views.MethodView):
	def get(self):
		return flask.render_template('sponsorship.html')