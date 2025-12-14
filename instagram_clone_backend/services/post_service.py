from app.db import posts_collection
from models.post_model import post_schema
from bson import ObjectId

def create_post(user_id: str, image_url: str, caption: str):
    post = post_schema(user_id, image_url, caption)
    post["_id"] = str(ObjectId())
    posts_collection.insert_one(post)
    return post


def get_post_by_id(post_id: str):
    return posts_collection.find_one({"_id": post_id})


def get_posts_by_user(user_id: str):
    return list(posts_collection.find({"user_id": user_id}).sort("created_at", -1))
