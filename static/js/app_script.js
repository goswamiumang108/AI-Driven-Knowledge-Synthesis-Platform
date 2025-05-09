document.addEventListener('DOMContentLoaded', () =>
{
	// Accessing the DOM elements
	const dragDropBox = document.getElementById('dragDropBox');
	const fileInput = document.getElementById('fileInput');
	const resourceList = document.getElementById('resourceList');
	const createKnowledgeBaseBtn = document.getElementById('createKnowledgeBaseBtn');
	const conversationBox = document.getElementById('conversationBox');
	const chatForm = document.querySelector('.chat-form');
	const chatInput = document.querySelector('.chat-input');
	const send_button = document.querySelector('.send-button');
	
	
	// Defining the initial state of the elements
	createKnowledgeBaseBtn.disabled = true;
	chatInput.disabled = true;
	send_button.disabled = true;
	
	// click on box → open file picker
	dragDropBox.addEventListener('click', () => fileInput.click());
	
	
	// drag over → add styling
	dragDropBox.addEventListener('dragover', e =>
	{
		e.preventDefault();
		dragDropBox.classList.add('drag-over');
	});
	
	// drag leave → remove styling
	dragDropBox.addEventListener('dragleave', () => dragDropBox.classList.remove('drag-over'));
	
	
	// drop → upload
	dragDropBox.addEventListener('drop', e =>
	{
		e.preventDefault();
		
		dragDropBox.classList.remove('drag-over');
		
		if (e.dataTransfer.files.length > 0)
		{
			uploadFile(e.dataTransfer.files[0]);
		}
	});
	
	
	// file picker change → upload
	fileInput.addEventListener('change', () =>
	{
		if (fileInput.files.length > 0)
		{
			uploadFile(fileInput.files[0]);
		}
	});
	
	
	function uploadFile(file)
	{
		const formData = new FormData();
		formData.append('file', file);
		
		fetch('/upload_resources', {method:'POST', body:formData})
			.then(response =>
			      {
				      if (!response.ok)
				      {
					      throw new Error(response.statusText);
				      }
				      return response.json();
			      })
			.then(result =>
			      {
				      // Remove the "empty state" if present
				      const empty = resourceList.querySelector('.panel-empty-state');
				      if (empty) empty.remove();
				      
				      // Append the new resource
				      const item = document.createElement('div');
				      item.className = 'resource-item';
				      item.textContent = result.filename || 'New Resource';
				      resourceList.appendChild(item);
				      
				      alert('Upload successful!');
				      createKnowledgeBaseBtn.disabled = false;
			      })
			.catch(err =>
			       {
				       console.error('Upload error:', err);
				       alert('Upload failed: ' + err.message);
			       });
	}
	
	function scrollToBottom()
	{
		conversationBox.scrollTop = conversationBox.scrollHeight;
	}
	
	chatForm.addEventListener('submit', async e =>
	{
		e.preventDefault();
		const text = chatInput.value.trim();
		if (!text) return;
		
		// Show user message
		const userMsg = document.createElement('div');
		userMsg.className = 'message user';
		userMsg.textContent = text;
		conversationBox.appendChild(userMsg);
		scrollToBottom();
		
		// Prepare for AI response
		chatInput.value = '';
		chatInput.disabled = true;
		send_button.disabled = true;
		
		try
		{
			const res = await fetch('/chat', {
				method:'POST',
				headers:{'Content-Type':'application/json'},
				body:JSON.stringify({message:text})
			});
			if (!res.ok) throw new Error('Server returned ' + res.status);
			
			const data = await res.json();
			const aiMsg = document.createElement('div');
			aiMsg.className = 'message ai';
			aiMsg.textContent = data.response || 'No response.';
			conversationBox.appendChild(aiMsg);
			scrollToBottom();
			
		}
		catch (err)
		{
			console.error(err);
			const errMsg = document.createElement('div');
			errMsg.className = 'message ai';
			errMsg.textContent = '⚠️ Error: ' + err.message;
			conversationBox.appendChild(errMsg);
			scrollToBottom();
			
		}
		finally
		{
			chatInput.disabled = false;
			send_button.disabled = false;
			chatInput.focus();
		}
	});
	
	createKnowledgeBaseBtn.addEventListener('click', () =>
	{
		fetch('/create_knowledgebase')
			.then(response =>
			      {
				      createKnowledgeBaseBtn.disabled = true;
				      
				      if (!response.ok)
				      {
					      throw new Error(response.statusText);
				      }
				      return response.json();
			      })
			.then(result =>
			      {
				      createKnowledgeBaseBtn.disabled = false;
				      alert('KnowledgeBase created successfully!');
				      
				      chatInput.disabled = false;
				      send_button.disabled = false;
			      })
			.catch(err =>
			       {
				       createKnowledgeBaseBtn.disabled = false;
				       console.error('Error creating KnowledgeBase:', err);
				       alert('Failed to create KnowledgeBase: ' + err.message);
			       });
	});
});