# Python Backend for AI-Driven Knowledge Synthesis Platform


from os import getenv, listdir, mkdir, path

import google.generativeai as genai
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS
from langchain_community.document_loaders import PyPDFLoader

# Configuring Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = path.relpath(".//uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
	
	if not path.exists(UPLOAD_FOLDER):
		mkdir(UPLOAD_FOLDER)
	
	file.save(path.join(app.config['UPLOAD_FOLDER'], file.filename))
	
	return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})


@app.route("/process_resources")
def process_resources():
	def process_pdf(pdf):
		pdf_loader = PyPDFLoader(file_path=pdf, extraction_mode="layout")
		
		if not path.exists("./resources"):
			mkdir("./resources")
		
		with open(file="./resources/" + str(path.basename(pdf)).removesuffix(".pdf") + ".txt", mode="w+", encoding="utf-8") as f:
			for page in pdf_loader.load():
				f.write(page.page_content.strip())
	
	for resource in listdir("./uploads"):
		if resource.endswith('.pdf'):
			process_pdf(resource)


if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=False, load_dotenv=True)
	CORS(app)
