import json
import os

HISTORY_FILE = "chat_memory/history.json"


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_history(history):

    # create folder if not exists
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def add_message(user, assistant):

    history = load_history()

    history.append({
        "user": user,
        "assistant": assistant
    })

    save_history(history)