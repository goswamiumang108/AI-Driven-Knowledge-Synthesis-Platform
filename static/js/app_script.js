document.addEventListener('DOMContentLoaded', () =>
{
	const dragDropBox = document.getElementById('dragDropBox');
	const fileInput = document.getElementById('fileInput');
	
	// Open file dialog on click
	dragDropBox.addEventListener('click', () =>
	{
		fileInput.click();
	});
	
	// Handle file input change
	fileInput.addEventListener('change', () =>
	{
		if (fileInput.files.length > 0)
		{
			uploadFile(fileInput.files[0]);
		}
	});
	
	// Add/remove drag-over class
	dragDropBox.addEventListener('dragover', (e) =>
	{
		e.preventDefault();
		dragDropBox.classList.add('drag-over');
	});
	
	dragDropBox.addEventListener('dragleave', () =>
	{
		dragDropBox.classList.remove('drag-over');
	});
	
	// Handle file drop
	dragDropBox.addEventListener('drop', (e) =>
	{
		e.preventDefault();
		dragDropBox.classList.remove('drag-over');
		
		const files = e.dataTransfer.files;
		if (files.length > 0)
		{
			fileInput.files = files; // optional, for syncing
			uploadFile(files[0]);
		}
	});
	
	// Upload file to server
	function uploadFile(file)
	{
		const formData = new FormData();
		formData.append('file', file);
		
		fetch('/upload_resources', {method:'POST', body:formData})
			.then(response =>
			      {
				      if (response.ok)
				      {
					      alert('Upload successful!');
				      }
				      else
				      {
					      alert('Upload failed: ' + response.statusText);
				      }
			      })
			.catch(error =>
			       {
				       console.error('Upload error:', error);
				       alert('An error occurred: ' + error.message);
			       });
	}
});