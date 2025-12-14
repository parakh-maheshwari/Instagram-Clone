from fastapi import APIRouter, HTTPException,Depends,Body
from services.user_service import create_user, authenticate_user
from app.dependencies import get_current_user
from services.post_service import get_posts_by_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup")
def signup(data: dict = Body(...)):
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        raise HTTPException(status_code=400, detail="All fields are required")

    user = create_user(username, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return {"message": "User registered successfully"}

@router.post("/login")
def login(data: dict = Body(...)):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Email and password required")

    token = authenticate_user(email, password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {
        "id": current_user["_id"],
        "username": current_user["username"],
        "email": current_user["email"],
        "followers_count": len(current_user["followers"]),
        "following_count": len(current_user["following"])
    }

@router.get("/{user_id}")
def get_user_profile(user_id: str):
    user = users_collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user["_id"],
        "username": user["username"],
        "followers_count": len(user["followers"]),
        "following_count": len(user["following"])
    }

