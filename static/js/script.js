document.addEventListener('DOMContentLoaded', function () {
    // Notebook data
    const notebooks = [
        {
            title: "Test",
            date: "Test",
            sources: 0,
            bgColor1: "#ffffff",
            bgColor2: "#f7e6cc"
        }
    ];

    // DOM elements
    const notebooksGrid = document.getElementById('notebooksGrid');
    const createNewBtn = document.getElementById('createNewBtn');

    // Create a notebook tile element
    function createNotebookTile(notebook) {
        const article = document.createElement('article');
        article.className = "notebook-tile";
        article.style.background = `linear-gradient(90deg, ${notebook.bgColor1} 0%, ${notebook.bgColor2} 100%)`;

        const contentDiv = document.createElement('div');
        contentDiv.className = "notebook-content";

        const h3 = document.createElement('h3');
        h3.className = "notebook-title";
        h3.textContent = notebook.title;
        contentDiv.appendChild(h3);

        const p = document.createElement('p');
        p.className = "notebook-meta";
        p.textContent = notebook.date && notebook.sources ?
            `${notebook.date} · ${notebook.sources} ${notebook.sources === 1 ? 'source' : 'sources'}` : "";
        contentDiv.appendChild(p);

        article.appendChild(contentDiv);
        return article;
    }

    // Render all notebooks
    function renderNotebooks() {
        if (!notebooksGrid) {
            console.error('Notebooks grid element not found');
            return;
        }

        notebooksGrid.innerHTML = "";
        notebooks.forEach(nb => {
            notebooksGrid.appendChild(createNotebookTile(nb));
        });
    }

    // Create a new notebook
    function createNewNotebook() {
        const newNotebook = {
            title: "New Notebook",
            date: new Date().toLocaleDateString('en-GB', {
                day: '2-digit',
                month: 'short',
                year: 'numeric'
            }),
            sources: 0,
            bgColor1: "#ffffff",
            bgColor2: "#d6e7ff"
        };
        notebooks.unshift(newNotebook);
        renderNotebooks();
    }

    // Initialize
    renderNotebooks();

    if (createNewBtn) {
        createNewBtn.addEventListener('click', createNewNotebook);
    } else {
        console.error('Create new button not found');
    }
});

// Function to handle the click event on the Try NotebookLM button
function tryNotebookLM() {
    window.open("/dashboard", "_blank");
}