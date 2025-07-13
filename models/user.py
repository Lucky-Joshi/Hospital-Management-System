from db import db
import bcrypt

def create_user(username, password, role):
    existing = db['users'].find_one({"username": username})
    if existing:
        return False
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    db['users'].insert_one({
        "username": username,
        "password": hashed,
        "role": role
    })
    return True

def validate_user(username, password):
    user = db['users'].find_one({"username": username})
    if user and bcrypt.checkpw(password.encode(), user['password']):
        return user  # Return full user object with role
    return None
