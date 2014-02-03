from flask import Flask
import settings

# Views
from home import Home
from aboutUs import AboutUs
from shows import Shows
from gallery import Gallery
from sponsorship import Sponsorship
from team import Team
from contactUs import ContactUs

# Initialize app
app = Flask(__name__)

# Import secret key
app.secret_key = settings.secret_key

# Routes
app.add_url_rule('/',
	view_func=Home.as_view('home'),
	methods=['GET'])
app.add_url_rule('/aboutUs',
	view_func=AboutUs.as_view('aboutUs'),
	methods=['GET'])
app.add_url_rule('/shows',
	view_func=Shows.as_view('shows'),
	methods=['GET'])
app.add_url_rule('/gallery',
	view_func=Gallery.as_view('gallery'),
	methods=['GET'])
app.add_url_rule('/sponsorship',
	view_func=Sponsorship.as_view('sponsorship'),
	methods=['GET'])
app.add_url_rule('/team',
	view_func=Team.as_view('team'),
	methods=['GET'])
app.add_url_rule('/contactUs',
	view_func=ContactUs.as_view('contactUs'),
	methods=['GET'])

# Run the app
app.run(debug=True)
