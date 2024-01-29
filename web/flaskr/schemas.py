from pydantic import BaseModel

#class BaseModel:
#    pass

# ----------------------------------------------
# User key= email but userId must be unique
class UserBase(BaseModel):
    pass

class UserCreate(BaseModel):
    email: str
    userId: str

class UserDelete(BaseModel):
    userId: str


class User(UserBase):
    email: str 
    userId: str 

    class Config:
        orm_mode = True

# ----------------------------------------------
# World - worldId is key

class WorldBase(BaseModel):
    worldName: str
    description: str

class WorldCreate(WorldBase):
    userId: str

class WorldDelete(UserBase):
    worldId: int

class WorldEdit(WorldBase):
    worldId: int

class World(WorldBase):
    worldId: int
    userId: str

    class Config:
        orm_mode = True

# ----------------------------------------------
# Game - gameId is key, create with worldId and userId


    

class GameCreate(BaseModel):
    worldId: int
    userId: str 

class GameDelete(BaseModel):
    gameId: int

class GameAction(BaseModel):
    actionId: int
    actionText: str

class GameItem(BaseModel):
    itemId: int
    itemText: str

class GameText(BaseModel):
    textId: int
    textText: str

class GamePlayResponse(BaseModel):
    gameId: int
    stepId: int
    status: str
    texts: list[GameText]
    actions: list[GameAction]
    items: list[GameItem]


class GamePlay(BaseModel):
    gameId: int
    actionId: int 
    itemId: int



class Game(BaseModel):
    gameId: int
    worldId: int 
    userId: str
    stepId: int
    status: str

    class Config:
        orm_mode = True