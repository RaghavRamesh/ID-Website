import flask, flask.views

class AboutUs(flask.views.MethodView):
	def get(self):
		return flask.render_template('aboutUs.html')