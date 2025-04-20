import time

import gradio as gr

# Mock data and state
initial_state = {"documents": [], "notes": "", "chat_history": [], "theme": "light"}


def update_theme(theme):
	return gr.themes.Default() if theme == "dark" else gr.themes.Base()


def process_document(file):
	# Mock document processing
	time.sleep(2)
	return f"Processed: {file.name}"


def ai_query(query, history):
	# Mock AI responses
	response = "Mock AI Response: This is a sample answer. [Source: Document1.pdf, Page 12]"
	history.append((query, response))
	return history, history


if __name__ == "__main__":
	with gr.Blocks(title="NotebookLM Clone", theme=update_theme(initial_state["theme"])) as app:
		# State management
		state = gr.State(value=initial_state)
		
		# Header
		with gr.Row():
			gr.Markdown("# NotebookLM Clone")
			theme_btn = gr.Button("Toggle Dark Mode")
		
		# Main panels
		with gr.Row():
			# Left Panel - Document Management
			with gr.Column(scale=1, min_width=250):
				file_upload = gr.File(label="Upload PDF", file_types=[".pdf"])
				doc_progress = gr.Text(label="Processing Status")
			
			# Center Panel - Note Taking
			with gr.Column(scale=2, min_width=600):
				note_editor = gr.Textbox(
					lines=25, label="Converse with your documents", placeholder="Start typing your notes...",
					elem_id="editor"
				)
				with gr.Row():
					gr.Button("Save")
					gr.Button("Format")
					gr.Dropdown(["Section 1", "Section 2"], label="Document Section")
			
			# Right Panel - AI Assistant
			with gr.Column(scale=1, min_width=250):
				chatbot = gr.Chatbot(label="AI Assistant", type="messages")
				ai_input = gr.Textbox(placeholder="Ask about your documents...")
				with gr.Row():
					gr.Button("Summarize")
					gr.Button("Verify Facts")
					gr.Button("Suggest Content")
		
		# Event handling
		file_upload.upload(process_document, inputs=file_upload, outputs=doc_progress)
		
		ai_input.submit(ai_query, inputs=[ai_input, chatbot], outputs=[chatbot, ai_input])
	
	app.launch()