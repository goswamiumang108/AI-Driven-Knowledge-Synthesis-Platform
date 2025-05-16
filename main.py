# Python Backend for AI-Driven Knowledge Synthesis Platform


# Standard library imports
from datetime import datetime as dt, timezone as tz
from os import getenv, mkdir, path, scandir, system
# Third-party imports
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS
from google import genai
# Langchain and related imports
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import CSVLoader, Docx2txtLoader, PyPDFLoader, TextLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import SystemMessage


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
EmbeddingFunction = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Setting up the Text Splitter
Docs_Splitter = RecursiveCharacterTextSplitter(strip_whitespace=True, length_function=len, chunk_size=10008, chunk_overlap=108)

# Initializing the Chat Model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-04-17", google_api_key=google_api_key)


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
	if 'file' not in request.files or request.files['file'].filename == '':
		return jsonify({'error': 'No file in the request'}), 400
	
	incoming_file = request.files['file']
	uploads_filepath = path.join(".//uploads/", str(path.splitext(incoming_file.filename)[0]) + dt.now(tz.utc).strftime("_%Y%m%d%H%M%S") + str(
		path.splitext(incoming_file.filename)[1]))
	
	if not path.exists("./uploads/"):
		mkdir("./uploads/")
	incoming_file.save(uploads_filepath)
	
	return jsonify({'message': 'File uploaded successfully', 'filename': incoming_file.filename})


@app.route('/create_knowledgebase')
def create_knowledgebase():
	system('rmdir /s /q ".//KnowledgeBase"')
	
	uploads_files = [path.relpath(ele) for ele in scandir("./uploads/") if path.isfile(ele)]
	Sources_Documents = []
	
	for file_path in uploads_files:
		file_name = path.basename(file_path)
		file_extension = path.splitext(file_name)[1].lower()
		
		# noinspection PyBroadException
		try:
			if file_extension in [".pdf"]:
				pdf_loader = PyPDFLoader(file_path=file_path, extraction_mode="layout")
				Sources_Documents.extend(pdf_loader.load())
			elif file_extension in [".txt"]:
				txt_loader = TextLoader(file_path=file_path, encoding="utf-8")
				Sources_Documents.extend(txt_loader.load())
			elif file_extension in [".md", ".yml", ".json", ".xml", ".yaml"]:
				pass
			elif file_extension in [".docx", ".doc"]:
				docx_loader = Docx2txtLoader(file_path=file_path)
				Sources_Documents.extend(docx_loader.load())
			elif file_extension in [".pptx", ".ppt"]:
				pass
			elif file_extension in [".csv"]:
				csv_loader = CSVLoader(file_path=file_path)
				Sources_Documents.extend(csv_loader.load())
			elif file_extension in [".xlsx", ".xls"]:
				pass
			else:
				continue
		except:
			continue
	
	KnowledgeBase = FAISS.from_documents(documents=Sources_Documents, embedding=EmbeddingFunction)
	KnowledgeBase.save_local(folder_path=".//KnowledgeBase//FAISS//")
	
	system('rmdir /s /q "./uploads"')
	
	return jsonify({'message': 'Knowledge base created successfully'})


@app.route('/chat', methods=['POST'])
def chat():
	try:
		# Parse the incoming JSON data
		data = request.get_json()
		if not data or 'message' not in data:
			return jsonify({'error': 'Invalid request, "message" field is required'}), 400
		
		user_message = str(data['message'])
		
		# Retrieve relevant documents from the knowledge base
		retrieved_docs = FAISS.load_local(
			folder_path=".//KnowledgeBase//FAISS//",
			allow_dangerous_deserialization=True,
			embeddings=EmbeddingFunction
		).similarity_search(query=user_message)
		
		prompt = SystemMessage()
		
		# Generate the AI's response using the prompt and retrieved documents
		messages = prompt.invoke({"question": user_message, "context": retrieved_docs})
		response = llm.invoke(messages)
		
		return jsonify({'response': response.content}), 200
	except Exception as e:
		return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
	system('rmdir /s /q "./uploads"')
	system('rmdir /s /q "./resources"')
	system('rmdir /s /q ".//KnowledgeBase"')
	
	CORS(app)
	app.run(host="0.0.0.0", debug=False, load_dotenv=True)