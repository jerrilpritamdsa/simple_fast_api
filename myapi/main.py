from fastapi import FastAPI, Depends
import schemas
import models 

from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import Base


#creates a database if we dont have it , using the create engine
Base.metadata.create_all(engine)

#create a function that will allow us to access database
#and get session so we can make request and update thing on the database
def get_session():
    
    session = SessionLocal()
    #got this from session maker in database file
    
    try:
        #Yield keyword in Python is similar to a return statement used for returning values or objects in Python. However, there is a slight difference. 
        # The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value
        yield session
        
    finally:
        session.close()




app = FastAPI()


@app.get("/")
def getItems(session:Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item


## first method to post
# @app.post("/")
# def addItem(task:str):
#     newId = len(Database.keys()) + 1
#     Database[newId] = {"task": task}
#     return Database


## second method to post
@app.post("/")
def addItem(task:str, session:Session = Depends(get_session)):
    # we are updateting the task attribute of the Item in models.py
    # task is the task receved from the request
    item = models.Item(task = task)
    
    #adding to the database
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item

## third method to post
# @app.post("/")
# def addItem(body = Body()):
#     newId = len(Database.keys()) + 1
#     Database[newId] = {'task':body['task']}
#     return Database


@app.put("/{id}")
def updateItem(id:int, task:str, session:Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    item.task = task
    session.commit()
    
    return item
    
@app.delete("/{id}")
def deleteItem(id:int, session:Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    session.delete(item)
    session.commit()
    session.close()
    
    items = session.query(models.Item).all()
    return items