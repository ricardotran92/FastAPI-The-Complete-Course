from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users


app = FastAPI()

models.Base.metadata.create_all(bind=engine) # This line automatically creates the database tables based on the ORM models defined in models.py

app.include_router(auth.router) # Include the auth router to the main FastAPI app
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)






# stop at: "\12. Large Production Database Setup\1. FastAPI Project Production DBMS.mp4"