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
	const loadingOverlay = document.getElementById('loadingOverlay');
	const titleEl = document.getElementById('notebookTitle');
	const savedTitle = localStorage.getItem('notebookTitle');
	
	if (savedTitle)
	{
		titleEl.textContent = savedTitle;
	}
	
	titleEl.addEventListener('blur', function ()
	{
		let val = titleEl.textContent.trim();
		if (!val) val = 'Untitled notebook';
		titleEl.textContent = val;
		localStorage.setItem('notebookTitle', val);
	});
	
	titleEl.addEventListener('keydown', function (e)
	{
		if (e.key === 'Enter')
		{
			e.preventDefault();
			titleEl.blur();
		}
	});
	
	// Tooltip element for the createKnowledgeBaseBtn and chat controls
	let tooltip;
	
	function showTooltip(msg, target)
	{
		if (tooltip) tooltip.remove();
		tooltip = document.createElement('div');
		tooltip.className = 'custom-tooltip';
		tooltip.textContent = msg;
		document.body.appendChild(tooltip);
		const rect = target.getBoundingClientRect();
		tooltip.style.left = rect.left + window.scrollX + rect.width / 2 - tooltip.offsetWidth / 2 + 'px';
		tooltip.style.top = rect.top + window.scrollY - tooltip.offsetHeight - 8 + 'px';
	}
	
	function hideTooltip()
	{
		if (tooltip)
		{
			tooltip.remove();
			tooltip = null;
		}
	}
	
	function showLoading()
	{
		if (loadingOverlay) loadingOverlay.style.display = 'flex';
	}
	
	function hideLoading()
	{
		if (loadingOverlay) loadingOverlay.style.display = 'none';
	}
	
	createKnowledgeBaseBtn.addEventListener('mouseenter', () =>
	{
		// Check if there are any resource items (excluding the section title and empty state)
		const hasResource = !!resourceList.querySelector('.resource-item');
		if (!hasResource)
		{
			showTooltip('Please upload sources first.', createKnowledgeBaseBtn);
		}
	});
	createKnowledgeBaseBtn.addEventListener('mouseleave', hideTooltip);
	
	// Tooltip for chat input and send button
	function chatDisabledTooltipHandler(e)
	{
		if (chatInput.disabled || send_button.disabled)
		{
			showTooltip('Please upload sources and create the knowledge base first.', e.currentTarget);
		}
	}
	
	chatInput.addEventListener('mouseenter', chatDisabledTooltipHandler);
	chatInput.addEventListener('mouseleave', hideTooltip);
	send_button.addEventListener('mouseenter', chatDisabledTooltipHandler);
	send_button.addEventListener('mouseleave', hideTooltip);
	
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
		
		showLoading();
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
					  hideTooltip(); // Hide tooltip if any after upload
					  hideLoading();
				  })
			.catch(err =>
				   {
					   console.error('Upload error:', err);
					   alert('Upload failed: ' + err.message);
					   hideLoading();
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
		showLoading();
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
					  hideLoading();
				  })
			.catch(err =>
				   {
					   createKnowledgeBaseBtn.disabled = false;
					   console.error('Error creating KnowledgeBase:', err);
					   alert('Failed to create KnowledgeBase: ' + err.message);
					   hideLoading();
				   });
	});
});
