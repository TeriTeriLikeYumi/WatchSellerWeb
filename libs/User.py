import os
from werkzeug.security import generate_password_hash, check_password_hash

class User():
    def __init__(self,username = None,password = None,id=None):
        self.username = username
        self.password = password
        self.id = None
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id
    
    @staticmethod
    def get_by_username(username):
        user = User(username)
        return user
    
    def validate_login(self,password_hash):
        return check_password_hash(password_hash, self.password)