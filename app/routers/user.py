from fastapi import status, Depends, HTTPException, Response, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/users", tags= ['Users'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.User)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)  #hashing user given password before storing it in db
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model= schemas.User)
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'user with id: {id} does not exist')
    
    return user
    