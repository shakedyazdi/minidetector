from sqlalchemy import Column, Integer, String, DateTime
from database import Base

#The response model for the web page

class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    mac = Column(String)
    ip = Column(String)
    last_seen = Column(DateTime)

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} MAC={self.mac} IP={self.ip} LAST_SEEN={self.last_seen}>'
