import flask, flask.views

class Team(flask.views.MethodView):
	def get(self):
		return flask.render_template('team.html')