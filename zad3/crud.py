from sqlalchemy.orm import Session
import models, schemas

def get_posts(db: Session):
    return db.query(models.Post).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# TEJ FUNKCJI PRAWDOPODOBNIE BRAKOWAŁO:
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def update_post(db: Session, post_id: int, post_update: schemas.PostCreate):
    db_post = get_post(db, post_id)
    if db_post:
        for key, value in post_update.model_dump().items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False

def create_comment(db: Session, comment: schemas.CommentCreate, post_id: int):
    db_comment = models.Comment(**comment.model_dump(), post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment