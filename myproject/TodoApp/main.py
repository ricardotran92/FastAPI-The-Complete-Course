from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine) # This line automatically creates the database tables based on the ORM models defined in models.py

app.include_router(auth.router) # Include the auth router to the main FastAPI app
app.include_router(todos.router)





# stop at: "\10. Authentication & Authorization\3. FastAPI Project Router Scale Todos File.mp4"