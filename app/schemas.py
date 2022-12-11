from datetime import datetime
from typing import Union
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserBase(BaseModel):
    email : EmailStr

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id : int
    created_at : datetime

    class Config:                   
        orm_mode = True            #pydantic's orm_mode will tell the pydantic model to read the data even if it is not a dict, but an ORM model.

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : User

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post : Post
    votes : int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Union[str, None]= None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1, ge=0)
