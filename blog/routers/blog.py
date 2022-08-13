from fastapi import APIRouter,Depends,status,HTTPException,Response
from blog import models,schema,database
from typing import List
from sqlalchemy.orm import Session
from blog.repository import blog
from blog.oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schema.Blog, db: Session = Depends(get_db),current_user: schema.User=Depends(get_current_user)):
    return blog.create(request,db)


@router.get('/',response_model=List[schema.ShowBLog])
def all_blogs(db: Session = Depends(get_db),current_user: schema.User=Depends(get_current_user)):
    return blog.get_all(db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db: Session = Depends(get_db),current_user: schema.User=Depends(get_current_user)):
    return blog.delete(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request: schema.Blog,db: Session = Depends(get_db),current_user: schema.User=Depends(get_current_user)):
    return blog.update(id,db,request)


@router.get('/{id}',status_code=200,response_model=schema.ShowBLog)
def get_one_blog(id:int,response: Response,db: Session = Depends(get_db),current_user: schema.User=Depends(get_current_user)):
    return blog.show(id,db)
