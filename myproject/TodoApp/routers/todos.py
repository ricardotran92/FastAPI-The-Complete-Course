from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path, APIRouter
from ..models import Todos
from ..database import SessionLocal
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user


router = APIRouter(
    prefix='/todos',
    tags=['todos']
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


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool



@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed') 
    
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all() # query(Todos) ~ SQL query: SELECT * FROM todos


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, db: db_dependency, 
                      todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))
    db.add(todo_model)
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, db: db_dependency, 
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)
                      ): 
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    
    db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()
    db.commit()



# stop at: "\09. API Request Methods\5. FastAPI Project Delete Request (Todo Project).mp4"