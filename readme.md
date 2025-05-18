## ABSTRACT
The AI-Driven Knowledge Synthesis Platform automates the transformation of unstructured data, such as PDFs, e-books, spreadsheets, and web articles, into structured, multimodal outputs including summaries, quizzes, flashcards, and podcasts. Leveraging Retrieval-Augmented Generation pipelines, LangChain orchestration, and transformer-based NLP models, the platform enables dynamic cross-document knowledge synthesis tailored to user roles like students, educators, and professionals. It utilises semantic embeddings stored in a FAISS vector database for accurate and efficient retrieval. The system features a Gradio-based web interface, Python backend, and cloud deployment via Microsoft Azure. Designed with scalability, personalisation, and automation in mind, the platform significantly reduces manual content curation time, enhances learning and training outcomes, and supports educational institutions and corporate environments with customizable AI-generated content.
# CHAPTER 1 – INTRODUCTION
## Introduction
In today's data-driven landscape, organisations face an overwhelming deluge of unstructured digital documents, including PDFs, spreadsheets, presentations, and reports, stored across diverse platforms and formats. Manually searching, extracting, and synthesizing meaningful information from this data is a laborious and inefficient process. Fortunately, the evolution of Natural Language Processing, semantic search, and vector databases has enabled the development of intelligent systems that can understand and retrieve relevant information with human-like efficiency.
This project presents the development of a Document Understanding and Retrieval System that leverages state-of-the-art AI frameworks like LangChain and vector databases such as FAISS, deployed and scaled on Azure cloud infrastructure. The system ingests diverse file formats, parsing them into semantic chunks, embedding them into vector space, and performing retrieval-augmented generation to intelligently answer queries.
The need for such a system is evident across enterprise settings, academic environments, legal research, and even personal productivity tools. This project aims to provide a modular, cloud-scalable solution that automates the ingestion, chunking, embedding, and retrieval of documents, producing contextual responses in real time.
The report details the full system design, from requirement analysis and architecture to UML diagrams, deployment models, and future scope. It also evaluates the system's performance on key parameters like speed, scalability, and usability.
## Problem Statement
Organizations and users regularly deal with unstructured documents in formats like PDFs, Word files, presentations, and spreadsheets. Extracting relevant information or answering specific questions from such documents remains a manual and inefficient task. Traditional keyword-based search engines often fail to grasp the semantic context, leading to poor results.
There is an urgent need for an AI-powered system that can intelligently understand document content, chunk it into meaningful segments, and store it in a format that supports fast, context-aware retrieval. Such a system should not only fetch relevant segments but also generate human-like responses based on the retrieved context.
This project aims to address this problem by building a scalable Document Understanding and Retrieval System that leverages semantic embeddings, retrieval-augmented generation, and multimodal output synthesis — all deployed on cloud infrastructure to ensure performance, scalability, and availability.
## Objective
- Automate content extraction from unstructured documents.
- Generate multimodal outputs like quizzes, summaries, flashcards, and podcasts.
- Enable cross-document synthesis and personalization.
- Support scalable deployment for institutions and enterprises.
## Modules of the System
The system is structured into several core modules, each tasked with a distinct stage in the document understanding and response generation pipeline. These modules work in coordination to deliver accurate, personalized, and multimodal outputs.
### Document Ingestion
This module is responsible for the initial processing of documents in various formats, such as PDFs, Word documents, spreadsheets, and presentation slides. It includes functionalities for:
1. Uploading documents via user interfaces or APIs.
2. Converting them into machine-readable text using OCR (for scanned files) or parsers.
3. Organizing documents into a consistent internal structure for downstream processing.
### Knowledge Extraction
Once documents are ingested, this module processes the raw content to extract meaningful semantic units. It includes:
1. Text segmentation (or chunking) using natural language processing techniques.
2. Metadata extraction such as headings, authorship, and timestamps.
3. Entity recognition and relation extraction to build a structured knowledge representation.
### Cross-Document Retrieval
This module enables semantic search across multiple documents by leveraging vector-based similarity measures. It includes:
1. Generating embeddings for each document chunk using transformer-based models.
2. Storing these embeddings in a vector database (e.g., FAISS) for fast nearest-neighbour retrieval.
3. Accepting user queries and retrieving the most contextually relevant chunks across the document corpus using a Retrieval-Augmented Generation (RAG) approach.
### Multimodal Response Generation
After retrieving the relevant content, this module uses generative AI models (like GPT) to synthesize responses in various formats:
1. Textual summaries and explanations.
2. Interactive quizzes based on extracted key points.
3. Flashcards for revision and learning.
4. Audio outputs or podcast scripts for auditory consumption.
## Scope
The goal of this project is to design, develop, and deploy an AI-powered document understanding system using a Retrieval-Augmented Generation pipeline. The system is built to handle a variety of document formats, including PDFs, spreadsheets, and presentation slides, and enables end-to-end semantic search and synthesis capabilities.
Key components include:
1. **Document Ingestion:** Upload and preprocess multiple document types from users.
2. **Semantic Chunking:** Parse documents into meaningful text segments using natural language processing (NLP).
3. **Vector Embedding and Storage:** Generate and store semantic embeddings in a FAISS vector database for efficient retrieval.
4. **Query Processing & Retrieval:** Accept user queries and retrieve contextually relevant document segments using a RAG architecture.
5. **Response Generation:** Use generative AI models to synthesize coherent, informative, and multimodal responses.
6. **Cloud Deployment:** Implement the entire system on Microsoft Azure with features such as auto-scaling, caching, load-balancing, and high availability.
The system is engineered to support scalable, rapid-response, and robust performance capabilities for enterprise-level applications such as knowledge management, research automation, legal document analysis, and customer support.
# CHAPTER 2 – LITERATURE SURVEY
## Existing System
In recent years, the integration of artificial intelligence in education and productivity platforms has seen a rise. However, most of the existing systems offer limited and fragmented functionalities. For instance:
- **Quizlet:** a widely used platform, enables users to create flashcards manually. While it supports learning through spaced repetition and collaborative usage, it is heavily dependent on user-generated content and lacks any advanced automation or AI-based synthesis capabilities.
- **Grammarly:** another prevalent tool, focuses primarily on grammar checking and language refinement. Although powered by NLP techniques, its scope is narrowly limited to writing enhancement and does not cater to knowledge extraction or multimodal content creation.
Furthermore, traditional document summarization tools are generally single- format focused and lack the capability to process and integrate information across multiple types of documents such as PDFs, spreadsheets, and web pages.
### Limitations in Existing Systems
- No support for cross-format knowledge synthesis.
- Lack of personalized or dynamic output generation.
- Minimal or no use of advanced AI-based document retrieval and synthesis pipelines.
- Outputs are either static or user-dependent with little automation.
## Proposed System
The proposed AI-Driven Knowledge Synthesis Platform is an intelligent, cloud-based solution designed to automate the processes of document understanding, knowledge extraction, and multimodal output generation. Unlike traditional siloed tools such as basic summarizers, grammar checkers, or flashcard creators, this platform offers a unified workflow powered by advanced Natural Language Processing and Retrieval-Augmented Generation techniques.
At the core, the system enables users to upload diverse document types, including PDFs, spreadsheets, and presentations. These documents are parsed and semantically segmented into meaningful chunks using LangChain-orchestrated models. Each chunk is transformed into a high-dimensional embedding vector and stored in a FAISS vector database, facilitating context-aware semantic search. When a user submits a query, the system retrieves the most relevant document segments using both keyword and vector similarity and passes them through a generative language model to produce human-like responses.
The key differentiator of this system is its capacity to generate multimodal outputs—including textual summaries, quizzes, flashcards, and podcasts—tailored to diverse user roles such as students, educators, or corporate professionals. The entire application is containerized using Docker and deployed on Microsoft Azure, ensuring scalability, high availability, and seamless integration into institutional or enterprise environments. This proposed system thus addresses a critical gap in intelligent document processing and serves as a comprehensive, user-friendly, and scalable solution for modern knowledge management needs.
### Core Highlights
- **Document Parsing:** Ingests and converts diverse formats like PDFs, spreadsheets, e-books, and web articles into structured data.
- **Retrieval-Augmented Generation (RAG):** Uses semantic and keyword-based search to fetch relevant chunks from a document base, enabling high-quality content generation.
- **Multimodal Output Generation:** Automatically creates summaries, quizzes, flashcards, and even audio-based outputs (like podcasts) based on user needs.
The platform offers personalized output generation through role-based customization, and it ensures scalability via cloud deployment. Unlike existing tools, it leverages vector databases, LangChain orchestration, and transformer-based NLP models to provide a robust end-to-end solution.
### Feasibility Study
Feasibility analysis determines the viability of implementing the proposed system from multiple dimensions:
#### Technical Feasibility
The system leverages proven, open-source and cloud-compatible technologies:
- Transformers from Hugging Face for embedding and generation tasks.
- LangChain, which allows seamless orchestration of RAG pipelines.
- Vector databases (FAISS) for fast, similarity-based content retrieval.
- The backend is developed in Python, ensuring compatibility with popular AI frameworks.
Frontend is built using Gradio for fast and interactive user interfaces. These tools are mature, well-supported, and capable of handling real-time data processing and transformation.
#### Economic Feasibility
- Deployment via Microsoft Azure offers a flexible pricing model with pay-as- you-go plans, making it cost-efficient for academic institutions and startups.
- Open-source libraries and frameworks minimize initial development and licensing costs.
- Containerization using Docker enables portability and reduces infrastructure related expenditures.
- Thus, from a cost-benefit perspective, the system is economically viable for small teams and scalable enough for enterprise environments.
#### Operational Feasibility
- The interface is intuitive and accessible via a standard web browser, requiring no installation.
- Built using Gradio, it supports interactive document uploads, role-based personalization, and easy navigation.
- Since outputs are generated automatically using AI pipelines, users (educators, students, professionals) can benefit without requiring any technical background.
This makes the system practical and easy to integrate into existing academic and corporate workflows, ensuring high user acceptance and minimal learning curve.
# CHAPTER 3 – REQUIREMENTS ANALYSIS

## Requirement Analysis Method
The requirement analysis for this project involved a combination of interviews, observation, and document analysis to thoroughly understand user needs and system expectations. The approach comprised the following steps:
### Stakeholder Identification
- Identified key stakeholders such as end-users (students, researchers), system administrators, and technical teams involved in implementation.
### Requirement Gathering Techniques
- **Interviews & Questionnaires:** Conducted structured discussions with users to gather expectations about functionalities like document upload, search accuracy, response time, and system accessibility.
- **Document Study:** Reviewed technical papers and similar existing platforms to define benchmark features and non-functional needs.
- **Observation:** Simulated scenarios of document processing and query interactions to understand pain points and usability gaps.
### Requirement Categorization
- Clearly distinguished between Functional Requirements (FR) and Non-Functional Requirements (NFR).
- Each requirement was mapped to its corresponding system module to ensure traceability.
### Validation and Verification
- Requirements were verified against stakeholder feedback and validated for technical feasibility with the proposed technology stack (LangChain, FAISS, Azure).
## Data Requirements
- **Input:** PDFs, Word documents, spreadsheets, e-books
- **Output:** Summaries, Flashcards, Quizzes, Podcasts.
## Functional Requirements
Functional requirements establish the core behavior and capabilities that the system must provide to its users. These features are essential to the operation of the AI-Driven Knowledge Synthesis Platform, aligning with the system's objectives of enabling automated, multimodal knowledge synthesis. The following is a detailed list of the functional requirements:
### Document Upload and Ingestion
The system shall allow users to upload sources in various formats such as:
- PDF
- DOCX
- Excel sheets (XLSX/CSV)
- PowerPoint presentations (PPTX)
- E-books (EPUB)
- Web articles (via URL input)
- Uploaded documents shall be stored temporarily for processing and retrieval.
### Document Parsing and Preprocessing
- The platform shall extract raw text from uploaded documents using format- specific parsers.
- Content shall be segmented into semantically meaningful chunks using LangChain’s document chunking pipeline.
- Metadata such as title, author, and date shall be extracted where available.
### Semantic Embedding and Storage
- Each document chunk shall be converted into vector embeddings using pre-trained transformer models (e.g., BERT or Sentence-BERT).
- These embeddings shall be stored in a FAISS-based vector database to support similarity-based searches.
- The system shall ensure traceability by tagging each embedding with source document references.
### Query Input and Cross-Document Retrieval
- The system shall provide a query interface for users to input questions or topics of interest.
- Upon query submission, the system shall:
  - Perform keyword matching and vector similarity search.
  - Retrieve the most relevant document chunks from across all uploaded documents.
- The system shall present a ranked list of retrieved sources to ensure transparency.
### Multimodal Content Generation
The platform shall dynamically generate output in multiple formats:
- **Summaries:** Both extractive (keyword-based) and abstractive (language generation).
- **Quizzes:** Auto-generated MCQs based on key concepts extracted from documents.
- **Flashcards:** Generated in Q&A format for spaced-repetition learning.
- **Podcasts:** Summarized content converted to speech using text-to- speech APIs.
### Role-Based Personalization
- The system shall allow users to select roles (e.g., Educator, Student, Professional).
- Based on the selected role, output formatting, complexity, and tone shall be adapted. For example, educators may receive presentation slides, while students receive summaries and flashcards.
### User Authentication and Access Control
The system shall implement user authentication to support session-based access. Different access privileges shall be defined based on roles:
- **Admin:** Full access including user management and analytics.
- **General User:** Upload, query, and view outputs.
### Output Download and Sharing
Users shall be able to download generated outputs in popular formats:
- **Summaries and flashcards:** PDF or DOCX
- **Quizzes:** PDF or HTML
- **Podcasts:** MP3 or WAV
Outputs shall be optionally shareable via unique public URLs.
### Feedback Collection
- The system shall offer feedback mechanisms to rate the accuracy and relevance of outputs.
- This feedback shall be stored to improve future results via retraining or fine-tuning.
### System Logs and Monitoring
- All user activities (upload, query, generation) shall be logged for monitoring and analytics.
- Admin users shall be able to view system usage reports and error logs via a dashboard.
## Non-Functional Requirements
Non-functional requirements outline the performance characteristics, quality attributes, and constraints that the system must meet. These requirements ensure the system is usable, efficient, reliable, scalable, and secure - essential qualities for academic and professional adoption. The non-functional requirements for the AI-Driven Knowledge Synthesis Platform are categorized as follows:
### Performance Requirements
- The system shall process user queries and generate responses within a maximum latency of 3 seconds under normal load conditions.
- Embedding generation and document parsing for a standard document (less than 10MB) shall complete within 5–8 seconds.
- Simultaneous processing of at least 20 concurrent users shall be supported without degradation in performance on standard Azure VM configuration.
### Scalability
- The platform shall be horizontally scalable to accommodate increasing user loads, documents, and queries.
- It shall support auto-scaling of compute resources in the cloud (Azure) during peak usage.
- Modular architecture using microservices and containerization (via Docker) shall enable independent scaling of the document processing, embedding, retrieval, and generation modules.
### Reliability and Availability
- The system shall maintain 99.5% uptime, ensuring high availability for users across different time zones.
- All critical services shall be monitored using health checks, and failure recovery mechanisms (such as automatic restarts) shall be in place.
- Azure’s distributed infrastructure shall be leveraged to ensure redundancy and failover support.
### Usability
- The user interface shall be intuitive, clean, and responsive, making it accessible to users with minimal technical expertise.
- Instructions and tooltips shall be available for every major feature (e.g., file upload, output options).
- The platform shall support keyboard navigation, form validation, and mobile responsiveness for accessibility on tablets and smartphones.
### Maintainability
- The system architecture shall follow a modular structure, ensuring ease of updates and bug fixes.
- Code shall adhere to standard coding conventions (e.g., PEP 8 for Python).
- Version control shall be implemented via Git, with proper documentation for all modules to support collaborative development and future enhancement.
### Portability
- The application shall run in containerized environments and be deployable on any cloud platform (e.g., Azure, AWS, GCP) or on-premise system with Docker support.
- It shall be accessible across all major web browsers (Chrome, Firefox, Edge, Safari).
- No platform-specific features shall be hardcoded to ensure cross-platform compatibility.
### Security Requirements
- All data transmissions shall be encrypted using HTTPS with TLS 1.3.
- Uploaded documents shall be sandboxed and removed from storage after processing to ensure data privacy.
- Role-based access control (RBAC) shall be enforced to prevent unauthorized access to administrative functions.
- Authentication tokens (JWT or OAuth2) shall be used to secure user sessions.
- The system shall be regularly tested for vulnerabilities (e.g., XSS, CSRF, injection attacks).
### Compliance and Data Privacy
The system shall comply with applicable data protection regulations (e.g., GDPR, India’s DPDP Act) by ensuring:
- No long-term storage of personal documents or user data unless explicitly consented.
- Users can request deletion of their uploaded data at any time.
### Localization and Language Support
- The system shall support generation of outputs (summaries, quizzes, flashcards) in multiple languages (e.g., English, Hindi, Spanish) using multilingual models.
- The UI text shall be translatable based on user preference, supporting basic localization features.
### Auditability and Traceability
Every generated output (summary, quiz, podcast) shall be traceable to its source document chunks through unique identifiers. All user activities (uploads, queries, downloads) shall be logged with timestamps to support auditing.
## System Specifications
### Hardware
| **Component**   | **Specification**                      |
| --------------- | -------------------------------------- |
| Processor       | Intel Core i3 (10th Gen) or equivalent |
| Ram             | 4 GB                                   |
| Hard Disk       | 256 GB SSD                             |
| Network Adapter | 802.11 B/G/N Wireless or Ethernet      |
| Display         | 720p resolution monitor                |
| Input Devices   | Standard Keyboard and Mouse            |
### Software
Python, Flask, LangChain, HuggingFace Transformers, FAISS, Docker, Microsoft Azure.
# CHAPTER 4 – DESIGN
## Software Requirements Specification (SRS) Summary
The platform is designed to handle a diverse range of document formats, including PDFs, e-books, spreadsheets, presentations, and web articles. It employs advanced natural language processing models and retrieval-augmented generation pipelines to extract, synthesize, and repurpose content into various outputs, such as summaries, quizzes, flashcards, and podcasts.
The system generates these outputs dynamically based on the user's input and role, ensuring a personalized and context-aware experience. It leverages technologies like LangChain for orchestration, Hugging Face Transformers for semantic understanding, and FAISS for efficient vector-based similarity searches. This ensures that the content is not only retrieved accurately but also generated in a way that aligns with the user's intent and learning objectives.
The system is expected to significantly reduce the time and effort required for manual content curation, improve the accuracy of cross-document knowledge synthesis, and deliver an engaging user experience through multimodal output delivery.
The platform is especially useful for academic institutions automating course material creation, professionals compiling reports and training modules, and organizations managing large volumes of informational content. Overall, the SRS presents the AI-Driven Knowledge Synthesis Platform as a forward-thinking, AI-powered solution that bridges the gap between unstructured knowledge sources and personalized, actionable insights.
This section summarises the key functional and non-functional requirements outlined in Chapter 3 and maps them to the high-level components of the system.

| **Requirement ID** | **Description**                                          | **Mapped Component**              |
| ------------------ | -------------------------------------------------------- | --------------------------------- |
| **FR-1**           | Upload documents in PDF, spreadsheet, presentation, etc. | Document Ingestion Service        |
| **FR-2**           | Parse and chunk documents into semantic units            | Document Parser (LangChain)       |
| **FR-3**           | Generate and store vector embeddings                     | Embedding Service & FAISS DB      |
| **FR-4**           | Retrieve relevant chunks via multimodal outputs          | Retrieval Engine (RAG)            |
| **NFR-1**          | Response time under 3 seconds                            | Caching & Load-Balancing Layer    |
| **NFR-2**          | Auto-scaling on Azure                                    | Azure Deployment & Scaling Groups |
| **NFR-3**          | High availability                                        | Azure Availability Sets           |
## Glossary
- **Chunk:** A semantically coherent segment of a document.
- **Embedding:** A dense numerical vector representing semantic content.
- **RAG (Retrieval-Augmented Generation):** A framework combining retrieval of relevant text snippets with generative models.
- **Multimodal Output:** Content generated in multiple formats (text, audio, flashcards).
## Supplementary Specifications
- **Security:** All document uploads and outputs are encrypted in transit via HTTPS; stored embeddings are encrypted at rest with Azure Key Vault.
- **Accessibility:** The UI complies with WCAG 2.1 AA guidelines.
- **Internationalization:** Supports English and Hindi localization.
## Use Case Mode
Figure 1– Use Case Diagram
## Conceptual Class Diagram
Figure 2 – Conceptual Class Diagram
## Activity Diagram
Figure 3 – Activity Diagram
## Data Flow Diagrams
Figure 4 – DFD Level 0
Figure 5– DFD Level 1
Figure 6 – DFD Level 2
## Database Design (ER Diagram)
Figure 7 – ER Diagram
# CHAPTER 5 – SYSTEM MODELING
## Detailed Class Diagram
Figure 8 – Detailed Class Diagram
## Interaction Diagrams
Figure 9 – Sequence Diagram
Figure 10 – Collaboration Diagram
## State Diagram
Figure 11 – State Diagram
## Activity Diagram
Figure 12 – Activity Diagram
## Object Diagram
Figure 13 – Object Diagram
## Component Diagram
Figure 14 – Component Diagram
## Deployment Diagram
Figure 15 – Deployment Diagram
## Testing

### Unit Testing
- **DocumentParserTests:** Verify correct chunking of PDF and DOCX inputs.
- **EmbeddingServiceTests:** Validate embedding vector dimensions and reproducibility.
### Functional Testing
- **End-to-End Tests:** Upload a sample research paper → request summary → verify summary contains key sections.
- **Performance Tests:** Ensure average query response < 3 seconds under 100 concurrent users.
# CHAPTER 6 – CONCLUSION & FUTURE WORK
## Limitations of the Project
### Dependency on Third-Party NLP Libraries
The platform relies heavily on open-source libraries such as Hugging Face Transformers, LangChain, and FAISS. While these tools offer powerful capabilities, they are subject to external updates and breaking changes. Any major version change in these dependencies may require substantial code refactoring or re-integration.
### Scalability Bottlenecks in Vector Database
As the number of processed documents and corresponding vector embeddings increases, the performance of the FAISS vector database may degrade without the implementation of techniques like sharding or hierarchical indexing. In its current form, the system is optimized for moderate-scale use but may require architectural upgrades to handle enterprise-level data volumes.
## Future Enhancements
To ensure the continued evolution, adaptability, and scalability of the platform, the following future enhancements are proposed:
### Domain-Specific Model Fine-Tuning
Incorporating fine-tuned versions of large language models trained on specific domains (e.g., legal, medical, or academic texts) can significantly improve the accuracy and contextual relevance of the synthesized outputs. This will also allow the system to adapt better to industry-specific terminology.
### Sharding and Replication for FAISS
To handle exponentially growing vector data, the system architecture should integrate sharding techniques across multiple FAISS instances and use replication strategies to ensure high availability and faster retrieval.
### Support for Additional Output Modalities
The current system supports summaries, flashcards, quizzes, and podcasts. In future iterations, it can be extended to generate interactive learning content such as mind-maps, infographic slides, and AI-generated instructional videos, making it even more engaging for learners.
### Administrative Dashboard with Analytics
A feature-rich analytics dashboard will be integrated to help administrators track system usage patterns, user engagement metrics, and content popularity. This will aid decision-making, resource allocation, and continuous improvement of the system.
# CHAPTER 7 – BIBLIOGRAPHY & REFERENCES
## BIBLIOGRAPHY & REFERENCES
\[1\] “Azure AI Search Documentation,” 25 February 2025. \[Online\]. Available: <https://learn.microsoft.com/en-us/azure/search/>. \[Accessed 10 March 2025\].

\[2\] “FAISS GitHub Wiki,” Meta AI Research, 24 February 2025. \[Online\]. Available: <https://github.com/facebookresearch/faiss/wiki>. \[Accessed 10 March 2025\].

\[3\] “Flask Documentation (3.1.x),” Pallets, 5 January 2025. \[Online\]. Available: <https://flask.palletsprojects.com>. \[Accessed 10 March 2025\].

\[4\] “LangChain Documentation,” LangChain, Inc., 30 January 2025. \[Online\]. Available: <https://python.langchain.com/docs/introduction/>. \[Accessed 10 March 2025\].

\[5\] “LangChain HuggingFace Integrations Documentations,” LangChain, Inc., 16 October 2024. \[Online\]. Available: <https://python.langchain.com/docs/integrations/providers/huggingface/>. \[Accessed 10 March 2025\].

\[6\] “LangChain Python API Reference,” LangChain Inc., 2 March 2025. \[Online\]. Available: <https://python.langchain.com/api_reference/>. \[Accessed 10 March 2025\].

\[7\] “Gradio Documentation,” Gradio, 9 March 2025. \[Online\]. Available: <https://www.gradio.app/docs>. \[Accessed 10 March 2025\].

\[8\] “Python 3.13.2 documentation,” 10 March 2025. \[Online\]. Available: <https://docs.python.org/3/>. \[Accessed 10 March 2025\].

\[9\] “GitHub Docs,” GitHub, Inc., \[Online\]. Available: <https://docs.github.com/en>. \[Accessed 10 March 2025\].
