from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"User_name {self.user_name}"
    
    def get_id(self):
        return (self.user_name)
    
    def get(user_name):
        if user_name in USERS:
            temp = USERS[user_name]
            return User(temp[0],temp[1])
        else: 
            return None

# Initialize USERS
USERS = {
            "admin@stc.com.sa" : ("admin@stc.com.sa", "admin1234!"),
            "sachin@stc.com.sa" : ("sachin@stc.com.sa", "sachin1234$")
        }
