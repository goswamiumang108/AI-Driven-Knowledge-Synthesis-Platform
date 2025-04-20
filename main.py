# Python Backend for AI-Driven Knowledge Synthesis Platform

# Importing necessary libraries
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS

# Configuring Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")
# Loading environment variables from .env file
load_dotenv(dotenv_path=".env")


# noinspection PyUnresolvedReferences
@app.route('/')
def home():
	return render_template("Home_Page.html")


@app.route('/dashboard')
def dashboard():
	return render_template("Dashboard.html")


@app.route('/about')
def about():
	return render_template("About.html")


@app.route('/creators')
def creators():
	return render_template("Creators.html")


@app.route('/documentation')
def documentation():
	return render_template("Project_Documentation.html")


@app.errorhandler(404)
def Error404(e):
	return render_template("Error_404.html"), 404


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=False, load_dotenv=True)
	CORS(app)