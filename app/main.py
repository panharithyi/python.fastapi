from fastapi import FastAPI
from typing import Optional, List
from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


# command to Disable SqlAlchemy create Engine
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_posts = [{"title":"python courses","content":"fastapi course","id":1},
# {"title":"machine learning course","content":"supervised learning","id":2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i , p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

@app.get("/")
async def root():
    return {"message": "welcome to fastapi turtion."}
# @app.post("/createposts_with_no_validation")
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"title {payload['title']} content {payload['content']}"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     # posts = db.query(models.Post)
#     # print(posts)
#     return{"data" : posts}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
