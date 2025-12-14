def user_schema(username, email, password):
    return {
        "username": username,
        "email": email,
        "password": password,
        "followers": [],
        "following": []
    }
