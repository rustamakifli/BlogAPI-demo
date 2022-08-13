from sqlalchemy.orm import Session
from blog import models,schema
from fastapi import HTTPException,status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request,db: Session):
    new_blog = models.Blog(title=request.title,body = request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int,db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id ==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'BLog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,request,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'BLog with id {id} not found')
    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
    return blog
