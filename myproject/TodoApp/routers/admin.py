from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from ..models import Todos
from ..database import SessionLocal
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user


router = APIRouter(
    prefix='/admin',
    tags=['admin']
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


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    return db.query(Todos).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model  = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()