from datetime import datetime

def comment_schema(user_id: str, username: str, text: str):
    return {
        "user_id": user_id,
        "username": username,
        "text": text,
        "created_at": datetime.utcnow()
    }
