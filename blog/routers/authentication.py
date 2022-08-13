from fastapi import APIRouter,status,HTTPException,Depends
from blog import schema,database,token,models
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from blog.hashing import Hash
from datetime import timedelta
from ..token import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub":user.email})
    return {"access_token": access_token,"token_type": "bareer"}