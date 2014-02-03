import flask, flask.views

class ContactUs(flask.views.MethodView):
	def get(self):
		return flask.render_template('contactUs.html')