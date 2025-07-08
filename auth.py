import json
import os
import time

USERNAME = "admin"
PASSWORD = "admin"
MAX_ATTEMPTS = 3
LOCK_DURATION = 300  
STATE_FILE = "login_state.json"

def load_login_state():
    if not os.path.exists(STATE_FILE):
        return {"fa": 0, "lock_until": 0}
    with open(STATE_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"fa": 0, "lock_until": 0}

def save_login_state(state):
    with open(STATE_FILE, "w") as file:
        json.dump(state, file)

def login():
    state = load_login_state()
    current_time = time.time()

    if current_time < state["lock_until"]:
        print( "Account locked.")
        return False

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful")
        state["fa"] = 0
        state["lock_until"] = 0
        save_login_state(state)
        return True
    else:
        state["fa"] += 1
        print("Invalid credentials")

        if state["fa"] >= MAX_ATTEMPTS:
            state["lock_until"] = current_time + LOCK_DURATION
            print("Too many attempts. Locked")

        save_login_state(state)
        return False
