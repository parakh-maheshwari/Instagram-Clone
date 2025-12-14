from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from services.follow_service import follow_user, unfollow_user

router = APIRouter(prefix="/users", tags=["Follow"])

@router.post("/{user_id}/follow")
def follow(user_id: str, current_user=Depends(get_current_user)):
    success, message = follow_user(current_user["_id"], user_id)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}


@router.post("/{user_id}/unfollow")
def unfollow(user_id: str, current_user=Depends(get_current_user)):
    success, message = unfollow_user(current_user["_id"], user_id)
    if not success:
        raise HTTPException(status_code=400, detail=message)
    return {"message": message}
