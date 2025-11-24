# chat_store.py

import json
import os

CHAT_FILE = "chat_history.json"

def save_message(role, content):
    history = get_chat_history()
    history.append({"role": role, "content": content})
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def get_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def clear_chat():
    if os.path.exists(CHAT_FILE):
        os.remove(CHAT_FILE)
