import json
import bcrypt
import os

DB_FILE = "auth/users.json"

os.makedirs("auth", exist_ok=True)

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)


def load_users():
    with open(DB_FILE) as f:
        return json.load(f)


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)


def register_user(email, password):

    users = load_users()

    if email in users:
        return False

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    users[email] = hashed
    save_users(users)

    return True


def login_user(email, password):

    users = load_users()

    if email not in users:
        return False

    stored = users[email].encode()

    return bcrypt.checkpw(password.encode(), stored)