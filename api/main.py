from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    return [{"item_id": 1, "q": "quesion1"},{"item_id": 2, "q": "question2"} ]



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/world")
def get_worlds():
        data = [{"id":"1", "name":"tara", "description":"taraking","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"2", "name":"bd", "description":"a bd","tags":"tag1,tag2", "numlines":4, "numerrors":0}, 
            {"id":"3","name":"dinah", "description":"a dinahshore","tags":"tag1,tag2", "numlines":4, "numerrors":0}]
        return data
