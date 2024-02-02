from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    userId = Column(String, primary_key=True, index=True, unique=True)
    email = Column(String, primary_key=False, index=True)

    worlds = relationship("World", back_populates="user")

class World(Base):
    __tablename__ = "worlds"

    worldId = Column(Integer, primary_key=True, index=True)
    worldName = Column(String, unique=False, index=False)
    description= Column(String, unique=False, index=False)
    userId = Column(String, ForeignKey("users.userId"))
    
    user = relationship("User", back_populates="worlds")



class Game(Base):
    __tablename__ = "games"

    gameId = Column(Integer, primary_key=True, index=True)
    userId = Column(String, index=True)
    worldId = Column(Integer, index=True)
    status = Column(String, index=True)
    step = Column(Integer, index=True)
