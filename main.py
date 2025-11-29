import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
database = []

class Item(BaseModel):
    value: int


@app.get("/")
def read_root():
    return {"message": "Hello world"}


@app.get("/items")
def read_items():
    return database


@app.post("/items")
def create_items(item: Item):
    database.append(item.dict())  
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    database[item_id] = item.dict()
    return item


@app.delete("/items/{item_id}")
def delete_items(item_id: int):
    del database[item_id]
    return {"message": "item deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
