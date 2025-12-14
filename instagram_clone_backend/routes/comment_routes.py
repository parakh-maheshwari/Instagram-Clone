from fastapi import APIRouter, Depends, Body, HTTPException
from app.dependencies import get_current_user
from services.comment_service import add_comment, get_comments

router = APIRouter(prefix="/posts", tags=["Comments"])

@router.post("/{post_id}/comment")
def comment_on_post(
    post_id: str,
    data: dict = Body(...),
    current_user=Depends(get_current_user)
):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    success = add_comment(
        post_id,
        current_user["_id"],
        current_user["username"],
        text
    )

    if not success:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"message": "Comment added"}


@router.get("/{post_id}/comments")
def fetch_comments(post_id: str):
    comments = get_comments(post_id)
    if comments is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return comments
