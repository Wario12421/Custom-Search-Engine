from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Load crawled URLs from the JSON file
file_path = "urls.json"
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)  # Create an empty list if the file doesn't exist

with open(file_path) as f:
    try:
        urls = json.load(f)
    except json.JSONDecodeError:
        urls = []  # If the file is empty or contains invalid JSON, use an empty list

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        results = [url for url in urls if query in url.lower()]
        return render_template("search_results.html", results=results)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)