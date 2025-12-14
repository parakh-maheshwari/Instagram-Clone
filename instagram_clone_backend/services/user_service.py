from app.db import users_collection
from app.auth import hash_password, verify_password, create_access_token
from bson import ObjectId

def create_user(username, email, password):
    if users_collection.find_one({"email": email}):
        return None

    user = {
        "_id": str(ObjectId()),
        "username": username,
        "email": email,
        "password": hash_password(password),
        "followers": [],
        "following": []
    }
    users_collection.insert_one(user)
    return user

def authenticate_user(email, password):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        return None

    token = create_access_token({"user_id": user["_id"]})
    return token
