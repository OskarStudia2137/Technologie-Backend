from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/posts", response_model=list[schemas.Post])
def read_posts(db: Session = Depends(database.get_db)):
    return crud.get_posts(db)

@app.post("/posts", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    return crud.create_post(db, post)

@app.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(database.get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.put("/posts/{post_id}", response_model=schemas.Post)
def update_post(post_id: int, post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    db_post = crud.update_post(db, post_id, post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(database.get_db)):
    if not crud.delete_post(db, post_id):
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/{post_id}/comments", response_model=schemas.Comment)
def create_comment_for_post(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.create_comment(db, comment, post_id)