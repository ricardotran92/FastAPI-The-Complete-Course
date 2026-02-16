from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users


app = FastAPI()

Base.metadata.create_all(bind=engine) # This line automatically creates the database tables based on the ORM models defined in models.py

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router) # Include the auth router to the main FastAPI app
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)





# Using relative diretory: 
# Ricardo@RICARDO-MSI MINGW64 ./myproject (main)
# $ uvicorn TodoApp.main:app --reload

# stop at: "\14. Project 4 - Unit & Integration Testing\24. Pytest - FastAPI Project Test Part 11.mp4"