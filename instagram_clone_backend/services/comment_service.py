from app.db import posts_collection
from datetime import datetime

def add_comment(post_id, user_id, username, text):
    post = posts_collection.find_one({"_id": post_id})
    if not post:
        return False

    comment = {
        "user_id": user_id,
        "username": username,
        "text": text,
        "created_at": datetime.utcnow()
    }

    posts_collection.update_one(
        {"_id": post_id},
        {"$push": {"comments": comment}}
    )
    return True


def get_comments(post_id):
    post = posts_collection.find_one({"_id": post_id})
    if not post:
        return None
    return post.get("comments", [])
