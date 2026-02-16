# contain reusable code for testing
from sqlalchemy import create_engine, text # text: run raw SQL
from sqlalchemy.pool import StaticPool # ensure SQL in-memory/testDB does not reset each new session creation
from sqlalchemy.orm import sessionmaker
from ..database import Base # create table
from ..main import app
from fastapi.testclient import TestClient # simulation for HTTP request
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrypt_context


SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass = StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # create session for DB test

Base.metadata.create_all(bind=engine) # init table based on models

def override_get_db():
    """When running a test, we use this dependency injection, we need to override the get_db() call"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'codingwithricardobytest', 'id': 1, 'user_role': 'admin'}


client = TestClient(app) # init client for API call

@pytest.fixture # setup test in advance
def test_todo():
    todo = Todos(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1
    ) # create object model
    # insert into db test
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    # return object for function test
    yield todo
    # cleanup after test → no affect to next tests
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        username="codingwithricardotest",
        email="codingwithricardotest@email.com",
        first_name="Ricardo",
        last_name="Tran",
        hashed_password=bcrypt_context.hash("testpassword"),
        role="admin",
        phone_number="(111)-111-1111"
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
