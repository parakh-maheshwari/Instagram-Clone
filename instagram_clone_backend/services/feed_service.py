from app.db import users_collection, posts_collection

def get_feed_for_user(user_id: str):
    user = users_collection.find_one({"_id": user_id})

    if not user:
        return []

    following_ids = user.get("following", [])

    # If user follows nobody, feed is empty
    if not following_ids:
        return []

    posts = posts_collection.find(
        {"user_id": {"$in": following_ids}}
    ).sort("created_at", -1)

    feed = []

    for post in posts:
        feed.append({
            "post_id": post["_id"],
            "user_id": post["user_id"],
            "image_url": post["image_url"],
            "caption": post["caption"],
            "likes_count": len(post["likes"]),
            "comments_count": len(post["comments"]),
            "created_at": post["created_at"]
        })

    return feed
