from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from retriever import create_faiss_index, retrieve_documents
from generator import generate_response

app = Flask(__name__)
UPLOAD_FOLDER = "data/documents/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handles document upload and indexing."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    # Process & index the document
    create_faiss_index()

    return jsonify({"message": "File uploaded and indexed successfully!"})

@app.route("/ask", methods=["POST"])
def ask():
    """Handles user questions based on uploaded documents."""
    data = request.json
    query = data.get("question", "").strip()

    if not query:
        return jsonify({"error": "No question provided"}), 400

    print(f"\n📥 Received Question: {query}")

    # Retrieve relevant documents
    retrieved_docs = retrieve_documents(query)
    if not retrieved_docs:
        return jsonify({"error": "No relevant information found in documents"}), 400

    print(f"📄 Retrieved Documents: {retrieved_docs}")

    # Generate response
    try:
        full_query = "\n".join(retrieved_docs) + "\n" + query
        print(f"⚡ Processing Query: {full_query}")

        answer = generate_response(full_query)
        print(f"✅ Generated Answer: {answer}")

        return jsonify({"answer": answer})  # ✅ Return response to webpage
    except Exception as e:
        print(f"❌ Error in generate_response: {str(e)}")
        return jsonify({"error": "Failed to generate answer"}), 500

if __name__ == "__main__":
    app.run(debug=True)
