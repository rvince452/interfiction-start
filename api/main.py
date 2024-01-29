from typing import Union

from fastapi import FastAPI, Depends, HTTPException, Header, Request
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import crud, models, schemas
from typing import Annotated

models.Base.metadata.create_all(bind=engine)
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return [{"item_id": 1, "q": "quesion1"},{"item_id": 2, "q": "question2"} ]



@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_user_from_token(user_token:str)->str:
    return user_token

def get_user_from_header(usertoken: Annotated[str | None, Header()]):
    user = get_user_from_token(usertoken)
    return user

def get_user(user: str = Depends(get_user_from_header))-> str:
    return user

def get_authorized_user(user: str = Depends(get_user))-> str:
    if not user or user == "user__":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user

def check_user_can_edit_user(db: Session, user: str, user_to_edit: str)-> bool:
    if user == user_to_edit:
        return True
    return False

def check_user_can_edit_world(db: Session, user: str, worldId: int)-> bool:
    return False 

def check_user_can_edit_game(db: Session, user: str, gameId: int)-> bool:
    return False 


@app.get("/usertest/")
def test_user(user: str = Depends(get_authorized_user)
    #db: Session = Depends(get_db),
    #            user_token: Annotated[str | None, Header()] = None
    ) -> str:
    #authorize_user_token(user_token)
    return user

# ----------------------------------------------------

@app.post("/user/") #, response_model=schemas.User)
def create_user(user: schemas.UserCreate, request: Request,  db: Session = Depends(get_db),
                username:str = Depends(get_authorized_user)):
                
    db_user = crud.get_user_by_id(db, userId=user.userId)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)
    #return user.userId


@app.get("/user/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.delete("/user/", response_model=schemas.User)
def delete_user(user: schemas.UserDelete, db: Session = Depends(get_db)):
    # TODO: check if user is authorized to delete
    # TODO: delete all worlds and games
    users = crud.delete_user(db, user=user)
    return users

# ----------------------------------------------------

@app.get("/world/", response_model=list[schemas.World])
def read_worlds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    worlds = crud.get_worlds(db, skip=skip, limit=limit)
    return worlds

@app.delete("/world/", response_model=schemas.World)
def delete_world(world: schemas.WorldDelete, db: Session = Depends(get_db)):
    worlds = crud.delete_world(db, world=world)
    # TODO - delete all related games
    return worlds

@app.put("/world/", response_model=schemas.World)
def edit_world(world: schemas.WorldEdit, db: Session = Depends(get_db)):
    worlds = crud.edit_world(db, world=world)
    return worlds


@app.post("/world/", response_model=schemas.World)
def create_world(world: schemas.WorldCreate, db: Session = Depends(get_db),
                  username:str = Depends(get_authorized_user)):
    return crud.create_world(db=db, world=world)

# ----------------------------------------------------

@app.get("/game/", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games

@app.delete("/game/", response_model=schemas.Game)
def delete_game(game: schemas.GameDelete, db: Session = Depends(get_db)):
    games = crud.delete_game(db, game=game)
    # TODO - delete all related games
    return games

@app.put("/game/", response_model=schemas.Game)
def play_game(game: schemas.GamePlay, db: Session = Depends(get_db)):
    # TODO - check if world is valid
    games = crud.edit_world(db, game=game)
    return games


@app.post("/game/", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)
