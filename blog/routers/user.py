from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from blog import database,models,schema
from blog.hashing import *
from blog.repository import user
router = APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db = database.get_db

@router.post('/',response_model=schema.ShowUser)
def create_user(request: schema.User,db: Session = Depends(get_db)):
    return user.create(request,db)


@router.get('/{id}',response_model=schema.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.get(id,db)
#running uvicorn blog.main:app --reload