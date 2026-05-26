import json


class AuthManager:
    def __init__(self):
        self.users = []
        self.attempts = 3
        self.current_user = None
        self.load_auth()

    def load_auth(self):
        try:
            with open("auth.json", "r") as f:
                data = json.load(f)
                self.users = data.get("users", [])
        except FileNotFoundError:
            self.users = []
            self.save_auth()

    def save_auth(self):
        with open("auth.json", "w") as f:
            json.dump({"users": self.users}, f, indent=5)

    def signup(self, username, password):
        for user in self.users:
            if user["username"] == username:
                return False

        self.users.append({"username": username, "password": password})

        self.save_auth()
        return True

    def login(self, username, password):

        for user in self.users:
            if user["username"] == username:

                if user["password"] == password:
                    self.current_user = username
                    self.attempts = 3
                    return True
                else:
                    self.attempts -= 1
                    if self.attempts <= 0:
                        return "blocked"
                    return False

        self.attempts -= 1
        if self.attempts <= 0:
            return "blocked"
        return False
