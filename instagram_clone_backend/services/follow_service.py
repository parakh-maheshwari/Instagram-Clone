from app.db import users_collection

def follow_user(current_user_id: str, target_user_id: str):
    if current_user_id == target_user_id:
        return False, "You cannot follow yourself"

    current_user = users_collection.find_one({"_id": current_user_id})
    target_user = users_collection.find_one({"_id": target_user_id})

    if not target_user:
        return False, "User not found"

    if target_user_id in current_user["following"]:
        return False, "Already following this user"

    users_collection.update_one(
        {"_id": current_user_id},
        {"$push": {"following": target_user_id}}
    )

    users_collection.update_one(
        {"_id": target_user_id},
        {"$push": {"followers": current_user_id}}
    )

    return True, "User followed successfully"


def unfollow_user(current_user_id: str, target_user_id: str):
    current_user = users_collection.find_one({"_id": current_user_id})
    target_user = users_collection.find_one({"_id": target_user_id})

    if not target_user:
        return False, "User not found"

    if target_user_id not in current_user["following"]:
        return False, "You are not following this user"

    users_collection.update_one(
        {"_id": current_user_id},
        {"$pull": {"following": target_user_id}}
    )

    users_collection.update_one(
        {"_id": target_user_id},
        {"$pull": {"followers": current_user_id}}
    )

    return True, "User unfollowed successfully"
