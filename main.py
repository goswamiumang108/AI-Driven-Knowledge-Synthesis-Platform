# Python Backend for AI-Driven Knowledge Synthesis Platform


from datetime import datetime, timezone
from os import getenv, mkdir, path, remove
import google.generativeai as genai
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS
from langchain_community.document_loaders import PyPDFLoader

# Configuring Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# Loading environment variables from .env file
load_dotenv(dotenv_path=".env")

CognitiveServices_Endpoint = getenv("CognitiveServices_Endpoint")
CognitiveServices_APIKey = getenv("CognitiveServices_APIKey")
google_api_key = getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)


# noinspection PyUnresolvedReferences
@app.route('/')
def home():
	return render_template("Home_Page.html")


@app.route('/app')
def web_app():
	return render_template("app.html")


@app.route('/about')
def about():
	return render_template("About.html")


@app.route('/creators')
def creators():
	return render_template("Creators.html")


@app.route('/documentation')
def documentation():
	return render_template("Project_Documentation.html")


# noinspection PyUnusedLocal
@app.errorhandler(404)
def Error404(e):
	return render_template("Error_404.html"), 404


@app.route(rule='/upload_resources', methods=['POST'])
def upload_files():
	if 'file' not in request.files:
		return jsonify({'error': 'No file part in the request'}), 400
	
	file = request.files['file']
	
	if file.filename == '':
		return jsonify({'error': 'No file selected'}), 400
	
	if not path.exists("./uploads"):
		mkdir("./uploads")
	
	file_path = path.join("./uploads", path.splitext(file.filename)[0]) + datetime.now(timezone.utc).strftime("_%Y%m%d%H%M%S") + str(path.splitext(file.filename)[1])
	file.save(file_path)
	
	if file.filename.endswith('.pdf'):
		process_resources("pdf", file_path)
		remove(file_path)
	
	return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})


def process_resources(resource_type, resource):
	if resource_type == "pdf":
		pdf_loader = PyPDFLoader(file_path=resource, extraction_mode="layout")
		if not path.exists("./resources"):
			mkdir("./resources")
		with open(file="./resources/" + str(path.splitext(resource)[0]) + ".txt", mode="w+", encoding="utf-8") as f:
			for page in pdf_loader.load():
				f.write(page.page_content.strip())


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=False, load_dotenv=True)
	CORS(app)
