# Python Backend for AI-Driven Knowledge Synthesis Platform


# Standard library imports
import shutil
from datetime import datetime as dt, timezone as tz
from os import getenv, mkdir, path, remove, scandir, system
# Third-party imports
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS
from google import genai
# Langchain and related imports
from langchain import hub
from langchain.chat_models import init_chat_model
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, CSVLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# Configuring Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# Loading environment variables from .env file
load_dotenv(dotenv_path=".env")

# Fetching environment variables
CognitiveServices_Endpoint = getenv("CognitiveServices_Endpoint")
CognitiveServices_APIKey = getenv("CognitiveServices_APIKey")
google_api_key = getenv("GOOGLE_API_KEY")

# Initializing the GenAI Client
GenAI_client = genai.Client(api_key=google_api_key)

# Setting up the Google Generative AI Embeddings
EmbeddingFunction = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Setting up the Text Splitter
Docs_Splitter = RecursiveCharacterTextSplitter(strip_whitespace=True, length_function=len, chunk_size=10008, chunk_overlap=108)

# Initializing the Chat Model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Setting up the RAG Prompt
prompt = hub.pull("rlm/rag-prompt")


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
	
	incoming_file = request.files['file']
	
	uploads_filepath = path.join(".//uploads/", str(
		path.splitext(incoming_file.filename)[0]) + dt.now(tz.utc).strftime("_%Y%m%d%H%M%S") + str(
		path.splitext(incoming_file.filename)[1]))
	
	processed_filepath = path.join(
		path.relpath("./resources/"), str(path.splitext(path.basename(uploads_filepath))[0]) + ".txt")
	
	if incoming_file.filename == '':
		return jsonify({'error': 'No file selected'}), 400
	
	if not path.exists("./uploads/"):
		mkdir("./uploads/")
	
	incoming_file.save(uploads_filepath)
	
	if not path.exists("./resources"):
		mkdir("./resources")
	
	file_extension = path.splitext(incoming_file.filename)[1].lower()
	if file_extension in [".pdf"]:
		pdf_loader = PyPDFLoader(file_path=uploads_filepath, extraction_mode="layout")
		with open(file=processed_filepath, mode="w+", encoding="utf-8") as f:
			for page in pdf_loader.load():
				f.write(page.page_content.strip())
	
	elif file_extension in [".txt"]:
		shutil.move(src=uploads_filepath, dst=processed_filepath)
		
	elif file_extension in [".md", ".yml", ".json", ".xml", ".yaml"]:
		pass
	
	elif file_extension in [".docx", ".doc"]:
		docx_loader = Docx2txtLoader(file_path=uploads_filepath)
		with open(file=processed_filepath, mode="w+", encoding="utf-8") as f:
			for page in docx_loader.load():
				f.write(page.page_content.strip())
	
	elif file_extension in [".pptx", ".ppt"]:
		pass
	
	elif incoming_file.filename.endswith(".csv"):
		csv_loader = CSVLoader(file_path=uploads_filepath)
		with open(file=processed_filepath, mode="w+", encoding="utf-8") as f:
			for page in csv_loader.load():
				f.write(page.page_content.strip())
	
	elif incoming_file.filename.endswith(".xlsx") or incoming_file.filename.endswith(".xls"):
		pass
	
	else:
		return jsonify({'message': 'File type not supported', 'filename': incoming_file.filename})
	
	remove(path=uploads_filepath)
	
	return jsonify({'message': 'File uploaded successfully', 'filename': incoming_file.filename})


@app.route('/create_knowledgebase')
def create_knowledgebase():
	Sources_Path = [path.relpath(ele) for ele in scandir("./resources/") if path.isfile(ele)]
	Sources = [open(file=ele, mode="r", encoding="utf-8").read() for ele in Sources_Path]
	Final_Sources = []
	
	for source in Sources:
		Final_Sources.extend(Docs_Splitter.split_text(text=source))
	
	Sources = [ele for ele in Final_Sources]
	
	KnowledgeBase = FAISS.from_texts(texts=Sources, embedding=EmbeddingFunction, docstore=InMemoryDocstore())
	KnowledgeBase.save_local(folder_path=".//KnowledgeBase//FAISS//")
	
	return jsonify({'message': 'Knowledge base created successfully'})


@app.route('/chat', methods=['POST'])
def chat():
	try:
		# Parse the incoming JSON data
		data = request.get_json()
		if not data or 'message' not in data:
			return jsonify({'error': 'Invalid request, "message" field is required'}), 400
		
		user_message = str(data['message'])
		
		retrieved_docs = FAISS.load_local(folder_path=".//KnowledgeBase//FAISS//", embeddings=EmbeddingFunction).similarity_search(user_message)
		
		messages = prompt.invoke({"question": user_message, "context": retrieved_docs})
		response = llm.invoke(messages)
		
		return jsonify({'response': response.content}), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
	system('rmdir /s /q "./uploads"')
	system('rmdir /s /q "./resources"')
	system('rmdir /s /q ".//KnowledgeBase//FAISS//"')
	
	CORS(app)
	app.run(host="0.0.0.0", debug=False, load_dotenv=True)