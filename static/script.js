document.getElementById("uploadForm").onsubmit = async function(event) {
    event.preventDefault();
    let fileInput = document.getElementById("fileInput").files[0];

    if (!fileInput) {
        alert("Please select a file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput);

    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let result = await response.json();
    document.getElementById("uploadStatus").innerText = result.message;
};

document.getElementById("askButton").onclick = async function() {
    let question = document.getElementById("questionInput").value;

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    let response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    });

    let result = await response.json();
    document.getElementById("response").innerText = result.answer;
};
