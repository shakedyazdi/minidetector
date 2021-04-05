import models
import schemas
from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal

app = FastAPI()


# Dependency
#Creates the session with the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Send a query to the server and display it on the API page

@app.get("/all", response_model=List[schemas.Entity])
def get_mac_ip(db: Session = Depends(get_db)):
    return db.query(models.Entity).offset(0).all()

@app.get("/routers", response_model=List[schemas.Router])
def get_mac_ip(db: Session = Depends(get_db)):
      return db.query(models.Entity.mac).group_by(models.Entity.mac).having(func.count() >= 3).offset(0).all()

@app.get("/lastseen", response_model=List[schemas.Entity])
def get_mac_ip(db: Session = Depends(get_db)):
      return db.query(models.Entity).order_by(desc(models.Entity.last_seen)).all()
