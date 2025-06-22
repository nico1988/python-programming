from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, status, Form
from fastapi.responses import RedirectResponse

item_list = []

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    # add item to the list
    item_list.append(item)
    return item

# return all items
@app.get("/items/", response_model=list[Item])
def read_items():
    return item_list

# test status code
@app.get("/status", status_code=status.HTTP_204_NO_CONTENT)
def get_status():
    return {"status": "ok"}

