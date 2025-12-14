from datetime import datetime

def post_schema(user_id: str, image_url: str, caption: str):
    return {
        "user_id": user_id,
        "image_url": image_url,
        "caption": caption,
        "likes": [],
        "comments": [],
        "created_at": datetime.utcnow()
    }
