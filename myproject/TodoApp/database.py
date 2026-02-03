# database.py is used to create URL string to connect FastAPI application to database (SQLite)
from sqlalchemy import create_engine # create_engine is used to set up the database connnection
from sqlalchemy.orm import sessionmaker # sessionmaker is used to create a new session for interacting with the database
from sqlalchemy.ext.declarative import declarative_base # declarative_base is used to create a base class for our ORM models

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
    # SQLite database URL format: sqlite:///./database_name.db → ./ means the database file will be created in the current directory

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
    # In FastAPI, it's very normal to have more than one thread that could interact with the database at the same time → SQLite do not check the same thread.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# bind=engine tells the sessionmaker which engine to use for database connections
# autocommit and autoflush are set to False to let us have fully control of everything our database session does → we will explicitly commit changes and flush data when needed.

Base = declarative_base() # Base class for our ORM models
