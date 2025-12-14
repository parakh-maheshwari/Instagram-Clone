from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from services.like_service import like_post, unlike_post

router = APIRouter(prefix="/posts", tags=["Likes"])

@router.post("/{post_id}/like")
def like(post_id: str, current_user=Depends(get_current_user)):
    success, message = like_post(post_id, current_user["_id"])
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}


@router.post("/{post_id}/unlike")
def unlike(post_id: str, current_user=Depends(get_current_user)):
    success, message = unlike_post(post_id, current_user["_id"])
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}
