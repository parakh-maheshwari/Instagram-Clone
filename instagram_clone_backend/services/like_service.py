from app.db import posts_collection

def like_post(post_id: str, user_id: str):
    post = posts_collection.find_one({"_id": post_id})

    if not post:
        return False, "Post not found"

    if user_id in post["likes"]:
        return False, "Post already liked"

    posts_collection.update_one(
        {"_id": post_id},
        {"$push": {"likes": user_id}}
    )

    return True, "Post liked"


def unlike_post(post_id: str, user_id: str):
    post = posts_collection.find_one({"_id": post_id})

    if not post:
        return False, "Post not found"

    if user_id not in post["likes"]:
        return False, "You have not liked this post"

    posts_collection.update_one(
        {"_id": post_id},
        {"$pull": {"likes": user_id}}
    )

    return True, "Post unliked"
