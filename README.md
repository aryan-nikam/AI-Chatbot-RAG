AI-Driven Chatbot using Retrieval-Augmented Generation (RAG)
📌 Overview
This project is an AI-powered chatbot that utilizes Retrieval-Augmented Generation (RAG) to answer user queries based on uploaded documents. It integrates FAISS-based document retrieval with transformer-based language models to generate accurate responses.

Why RAG?
Unlike traditional chatbots that rely solely on pre-trained knowledge, RAG enhances responses by retrieving relevant content from uploaded documents, ensuring:

Up-to-date information (based on the provided documents)
Context-aware responses
Improved accuracy over general-purpose language models
🚀 Key Features
✅ Retrieval-Augmented Generation (RAG): Combines retrieval-based and generation-based AI for accurate responses.
✅ FAISS-based document retrieval: Enables efficient search from large datasets.
✅ Transformer-based text generation: Uses OPT-1.3B for high-quality AI-generated responses.
✅ Optimized model loading: Uses BitsAndBytes and Accelerate for memory efficiency.
✅ Flask API with Web UI: Allows users to upload files and ask questions via a simple web interface.
✅ Multi-file support: Users can upload multiple documents for enhanced knowledge retrieval.

🛠 Tech Stack
Python: Flask, Transformers, FAISS, LangChain
Machine Learning & NLP: Hugging Face Transformers, FAISS for vector-based search
Frameworks: Flask (backend), Hugging Face (model integration), LangChain (retrieval)
Deployment: Works locally, can be extended to AWS, GCP, or Hugging Face Spaces

📂 Project Structure
├── backend/
│   ├── app.py               # Flask API to handle requests
│   ├── retriever.py         # FAISS document retriever
│   ├── generator.py         # AI-powered text generator
│   ├── data/documents/      # Folder to store uploaded files
│   ├── templates/index.html # Web UI template
├── README.md                # Project documentation
├── requirements.txt         # List of dependencies
├── venv/                    # Virtual environment (optional)
└── static/                  # Stores frontend assets like CSS & JS
🚀 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/aryan-nikam/AI-Chatbot-RAG
cd AI-Chatbot-RAG

2️⃣ Set Up a Virtual Environment
python -m venv venv
For Windows:
venv\Scripts\activate
For macOS/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python backend/app.py
This will start a local Flask server.

5️⃣ Open the Chatbot UI
Go to http://127.0.0.1:5000/ in your browser.
📝 How to Use
1️⃣ Upload a Document:

Click on the upload button and select a file.
The system indexes the document for retrieval.
2️⃣ Ask a Question:

Type a query related to the uploaded document.
The chatbot will retrieve relevant content and generate an AI-powered response.
3️⃣ View Responses:

The chatbot displays context-aware answers based on the uploaded documents.
⚡ Example Usage
Step 1: Upload a Document
📂 Example File Content (Deep_Learning_Notes.pdf):
Deep Learning is a subset of machine learning that uses artificial neural networks.
It has gained popularity due to its ability to learn patterns from large datasets.

Step 2: Ask a Question
🔎 User Question:
What is Deep Learning?
Step 3: AI-Generated Response
🤖 Chatbot Response:
Deep Learning is a branch of Machine Learning that uses artificial neural networks
to learn from data and identify patterns.

🛠 Model & Optimization
1️⃣ Transformer-Based Text Generation
Uses Facebook OPT-1.3B, a transformer-based language model for generating responses.
Can be replaced with a lighter model (e.g., distilgpt2) for faster performance.
2️⃣ FAISS for Document Retrieval
FAISS (Facebook AI Similarity Search) allows fast and efficient retrieval of relevant documents.
3️⃣ BitsAndBytes & Accelerate
Optimized model loading to reduce RAM and VRAM usage.
Works on CPU & low-resource devices.
🚀 Future Improvements
🔹 Cloud Deployment: Host the chatbot on AWS / Hugging Face Spaces.
🔹 Multi-Document Support: Improve retrieval from multiple files.
🔹 Streaming API: Implement real-time responses via WebSockets.
🔹 Lighter Models: Integrate GPT-2 Small / DistilBERT for improved speed.

🤝 Contributing
Want to improve this project? Contributions are welcome!

Steps to Contribute:
Fork the repository
Create a feature branch
    git checkout -b feature-branch

Make changes & commit
    git add .
    git commit -m "Added new feature"

Push & create a Pull Request
    git push origin feature-branch

📜 License
This project is open-source under the MIT License.

📧 Contact
📍 Author: Aryan Nikam
📩 Email: aryannikam030@gmail.com
🔗 GitHub: https://github.com/aryan-nikam