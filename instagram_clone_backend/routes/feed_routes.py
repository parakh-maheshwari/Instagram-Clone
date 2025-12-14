from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from services.feed_service import get_feed_for_user

router = APIRouter(tags=["Feed"])

@router.get("/feed")
def get_feed(current_user=Depends(get_current_user)):
    return get_feed_for_user(current_user["_id"])
