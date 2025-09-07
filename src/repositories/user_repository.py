import json
import os

def load_users():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "mock", "mock-users.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
