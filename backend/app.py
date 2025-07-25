# Import necessary modules
from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai

# Create a Flask application
# static_folder="../frontend" tells Flask where your HTML, CSS, and JS files are stored.
# static_url_path="/" means they will be served at the root URL (http://127.0.0.1:5000/).
app = Flask(__name__, static_folder="D:\Varmha_a6\1 Learm python\aitry\frontend", static_url_path="D:\Varmha_a6\1 Learm python\aitry\frontend")

# Your Gemini API Key (this allows you to connect to Google's Gemini AI model)
API_KEY = "AIzaSyDtCeRwSsZYyLT2Jcp9eQJ3-gZa9-utS1c"

# Configure the Gemini library with your API key
genai.configure(api_key=API_KEY)

# Select the Gemini model (gemini-2.0-flash is a fast version)
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session (like starting a conversation)
chat = model.start_chat()

# Route 1: Serve the main HTML file when someone visits "/"
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Route 2: Handle chat requests from the frontend
@app.route("/chat", methods=["POST"])
def chat_with_gemini():
    # Get the message from the user (sent from frontend via JSON)
    user_input = request.json.get("message")
    
    # Send the user message to Gemini and get its response
    response = chat.send_message(user_input)
    
    # Return the response as JSON (so frontend can display it)
    return jsonify({"response": response.text})

# Run the Flask app
# debug=True means auto-reload on code changes and show detailed error messages
if __name__ == "__main__":
    print("Starting Flask server at http://127.0.0.1:5000")
    print("Press CTRL+C to stop the server")
    app.run(debug=True)
