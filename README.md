🌟 AI ChatBot — Powered by Gemini or OpenAI APIs
# 🤖 AI ChatBot (Gemini/OpenAI Powered)

An intelligent chatbot built using Python that can work with **either the Google Gemini API key OR OpenAI API key**.  
This project allows you to switch between both models easily and interact with the chatbot through a simple interface.

---

## 🚀 Features
- 💬 Conversational chatbot using **Gemini** or **OpenAI** models  
- 🔄 Easily switch between APIs  
- ⚡ Fast responses  
- 🧠 Uses LLM (Large Language Model) to understand & generate text  
- 🔐 API keys stored securely in `.env` file  
- 🖥️ Simple Python codebase — beginner-friendly  

---

## 🛠️ Tech Used
- **Python 3**
- **Gemini API (Google AI Studio)**
- **OpenAI API**
- `dotenv` for environment variables  
- `requests` or official SDKs  
- Basic Flask (optional, if you add a web UI)

---

## 📁 Project Structure


AI-ChatBot/
│── chatbot.py
│── requirements.txt
│── .env # contains API keys (NOT uploaded to GitHub)
│── README.md


---

## 🔧 Setup Instructions

### 1️⃣ Clone the project  
```bash
git clone https://github.com/YOUR_USERNAME/AI-ChatBot.git
cd AI-ChatBot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your API keys

Create a file named .env in the project folder:

GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
MODEL_PROVIDER=gemini   # or openai


You can switch between models by changing:

MODEL_PROVIDER=gemini


or

MODEL_PROVIDER=openai

▶️ Running the ChatBot
python chatbot.py


You will see:

Bot is ready!
You: 


Type questions, press Enter, and the bot replies.

🤖 Example Usage

You:

Explain blockchain in simple words.


Bot:

Blockchain is a digital record book that stores information securely across many computers.

🔁 Switching Between Gemini and OpenAI

Open .env and modify:

Gemini:

MODEL_PROVIDER=gemini


OpenAI:

MODEL_PROVIDER=openai


No code changes needed.

📦 chatbot.py (Core Logic Example)
import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def chat_with_bot(prompt):
    if MODEL_PROVIDER == "gemini":
        genai.configure(api_key=GEMINI_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

    elif MODEL_PROVIDER == "openai":
        client = OpenAI(api_key=OPENAI_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]

print("Bot is ready!")
while True:
    user = input("You: ")
    reply = chat_with_bot(user)
    print("Bot:", reply)

📝 Future Enhancements

🌐 Add a Flask web UI

🎤 Add speech-to-text & text-to-speech

📚 Save chat history

🎨 Add a frontend (HTML/CSS/JS)

✨ Author

Lovely Pavithra G
Third-year Engineering | Cybersecurity | AI/ML | IoT | Blockchain learner

🌟 Final Note

“Programming isn't about what you know; it's about what you can figure out.” — Chris Pine


<img width="901" height="543" alt="Screenshot 2025-11-24 191839" src="https://github.com/user-attachments/assets/d45c8086-20f5-4f04-8df4-369196da52a6" />









<img width="905" height="567" alt="Screenshot 2025-11-24 191855" src="https://github.com/user-attachments/assets/7f10d9bf-73f6-4c37-bac7-9986f6c492fa" />


