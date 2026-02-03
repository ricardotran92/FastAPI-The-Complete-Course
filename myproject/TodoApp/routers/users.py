from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from models import Todos, Users
from database import SessionLocal
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/users',
    tags=['users']
)


def get_db():
    db = SessionLocal() # Create a new database session
    try: 
        yield db # return the session to be used in request handlers (endpoints)
    finally:
        db.close() # Ensure the session is closed after the request is done   


db_dependency = Annotated[Session, Depends(get_db)]
    # Annotated is a container; outer box labeling `Session` data type; inner box is Metadata, in this case, `Depends(get_db)`
    # Session is the type of the db parameter, indicating that it is a SQLAlchemy session
    # Depends is Dependency Injection, which allows us to define dependencies for our path operation functions
    # Dependency Injection means FastAPI will do something before and after the function is called (like creating and closing a database session)
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    return user_model


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, 
                          user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password=bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
    
    