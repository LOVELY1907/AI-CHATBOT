import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Short answer version
        prompt = (
            "You are Optimus Prime, a helpful AI assistant. "
            "Answer briefly in 2-3 sentences maximum. "
            "Keep replies simple, clear, and to the point.\n\n"
            f"User: {user_message}"
        )

        response = model.generate_content(prompt)
        bot_reply = response.text.strip()
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"})
