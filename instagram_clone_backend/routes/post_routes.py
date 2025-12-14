from fastapi import APIRouter, Depends, HTTPException,Body
from app.dependencies import get_current_user
from services.post_service import create_post, get_post_by_id
from services.post_service import get_posts_by_user

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_new_post(
    data: dict = Body(...),
    current_user=Depends(get_current_user)
):
    image_url = data.get("image_url")
    caption = data.get("caption", "")

    if not image_url:
        raise HTTPException(status_code=400, detail="image_url is required")

    post = create_post(current_user["_id"], image_url, caption)

    return {
        "message": "Post created successfully",
        "post_id": post["_id"]
    }


@router.get("/{post_id}")
def get_single_post(post_id: str):
    post = get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
