from typing_extensions import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
import models
from models import Todos
from database import engine, SessionLocal
from starlette import status
from pydantic import BaseModel, Field
from routers import auth, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine) # This line automatically creates the database tables based on the ORM models defined in models.py

app.include_router(auth.router) # Include the auth router to the main FastAPI app

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


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool



@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency): 
    return db.query(Todos).all() # query(Todos) ~ SQL query: SELECT * FROM todos


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()


@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)
                      ): 
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()



