from pydantic import BaseModel
from datetime import datetime

#Checks with Pydantic that the information is Valid

class Entity(BaseModel):
    mac: str
    ip: str
    last_seen: datetime

    class Config:
        orm_mode = True

class Router(BaseModel):
    mac: str
    
    class Config:
        orm_mode: True
