from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas

#----------------------------------------
# get_users
# get_user by email 
# get_user by id
# create_user
# delete_user PERMISSIONS



def get_user_by_id(db: Session, userId: str):
    return db.query(models.User).filter(models.User.userId == userId).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    #db_user = models.User(userId=user.userId, email = user.email)
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user: schemas.UserDelete):
    db_user = get_user_by_id(db, user.userId)
    db.delete(db_user)
    db.commit()
    return db_user

# ----------------------------------------------------
# get_worlds
# get_worlds by user
# get_world by id
# create_world
# delete_world PERMISSION
# edit_world PERMISSION


def get_worlds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.World).offset(skip).limit(limit).all()

def get_worlds_by_userId(db: Session, userId: str, skip: int = 0, limit: int = 100):
    return db.query(models.World).filter(models.World.userId == userId).offset(skip).limit(limit).all()


def get_world(db: Session, worldId: int):
    return db.query(models.World).filter(models.World.worldId == worldId).first()

def delete_world(db: Session, world: schemas.WorldDelete):
    db_obj = get_world(db, world.worldId)
    db.delete(db_obj)
    db.commit()
    return db_obj

def edit_world(db: Session, world: schemas.WorldEdit):
    db_obj = get_world(db, world.worldId)
    db_obj.worldName = world.worldName
    db_obj.description = world.description
    db.commit()
    db.refresh(db_obj)
    return db_obj

def create_world(db: Session, world: schemas.WorldCreate):
    if not get_user_by_id(db, world.userId):
        raise HTTPException(status_code=400, detail="User not registered")
    db_obj = models.World(**world.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


# ----------------------------------------------------
# get_games
# get_games by user
# get_game by id
# create_game
# delete_game PERMISSION
# play_game PERMISSION


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()

def get_games_by_userId(db: Session, userId: str, skip: int = 0, limit: int = 100):
    return db.query(models.Game).filter(models.Game.userId == userId).offset(skip).limit(limit).all()


def get_game(db: Session, gameId: int):
    return db.query(models.Game).filter(models.Game.gameId == gameId).first()

def delete_game(db: Session, game: schemas.GameDelete):
    db_obj = get_game(db, game.gameId)
    db.delete(db_obj)
    db.commit()
    return db_obj

def play_game(db: Session, game: schemas.GamePlay):
    db_obj = get_game(db, game.gameId)
    db_obj.status = "Playing"
    db.commit()
    db.refresh(db_obj)
    return db_obj

def create_game(db: Session, game: schemas.GameCreate):
    db_obj = models.Game(**game.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
