from sqlalchemy import create_engine, func, Column, String, Integer, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

db_string = "postgresql://detector:demo@db/minidetector"

engine = create_engine(db_string, pool_size=20, pool_timeout=300, max_overflow=-1)
Base = declarative_base()


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def create_session():
    return Session(bind=engine)


class Entity(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    mac = Column(String)
    ip = Column(String)
    last_seen = Column(DateTime)

    def __repr__(self):
        return f'<{self.__class__.__name__} id={self.id} MAC={self.mac} IP={self.ip} LAST_SEEN={self.last_seen}>'
