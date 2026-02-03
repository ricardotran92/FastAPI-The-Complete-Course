# models.py is a way for SQLAlchemy to understand what kind of database tables we are creating within database
from database import Base # Importing Base class from database.py to create ORM models
from sqlalchemy import Column, Integer, String, Boolean

""" todos Table Data

| Id (PK) | title               | description                     | priority | complete |
| ------- | ------------------- | ------------------------------- | -------- | -------- |
| **1**   | Go to store         | To pick up eggs                 | 4        | 0        |
| **2**   | Haircut             | Need to get length 1mm          | 3        | 0        |
| **3**   | Feed dog            | Make sure to use new food brand | 5        | 0        |
| **4**   | Water plant         | Inside and Outside plants       | 4        | 0        |
| **5**   | Learn something new | Learn to program                | 5        | 0        |
"""

class Todos(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
