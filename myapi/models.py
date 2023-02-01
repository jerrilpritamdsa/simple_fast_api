from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy object-relational configuration involves the combination of Table, mapper(),
# and class objects to define a mapped class.

Base = declarative_base()
#this when used in a class, returns a  base class from which all the mapped classes should inherit
#when we used this is the class Item,
# a new table and a mapper() function is generated
# which can be assessed using Item.__table and Item.__mapper__

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
    