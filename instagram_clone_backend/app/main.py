from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.follow_routes import router as follow_router
from routes.post_routes import router as post_router
from routes.like_routes import router as like_router
from routes.comment_routes import router as comment_router
from routes.feed_routes import router as feed_router

app = FastAPI(title="Instagram Mini Clone")

app.include_router(user_router)
app.include_router(follow_router)
app.include_router(post_router)
app.include_router(like_router)
app.include_router(comment_router)
app.include_router(feed_router)

@app.get("/")
def health_check():
    return {"status": "OK"}
