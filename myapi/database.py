from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#create database engine if there doesnt exist one
engine = create_engine('sqlite:///todo.db')

#sessionmaker class is normally used to create a top level Session configuration 
# which can then be used throughout an application without the need to repeat the configurational arguments.
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
#the Session establishes all conversations with the database and represents a “holding zone” 
# for all the objects which you’ve loaded or associated with it during its lifespan. 
# It provides the entrypoint to acquire a Query object, which sends queries to the database 

