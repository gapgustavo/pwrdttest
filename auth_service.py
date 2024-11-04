import secrets
from firebase_db import FirebaseDB

class AuthService:
    def __init__(self):
        self.db = FirebaseDB()

    def create_account(self, username, password):
        api_key = secrets.token_hex(25)
        return self.db.create_user(username, password, api_key), api_key

    def login(self, username, password):
        return self.db.login_user(username, password)

    def is_valid_api_key(self, api_key):
        return self.db.validate_api_key(api_key)
