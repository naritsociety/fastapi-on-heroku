from fastapi import FastAPI
from pymongo import MongoClient
from enum import Enum
from typing import Optional
# import datetime

app = FastAPI()

client = MongoClient("mongodb+srv://narit:Crazydog2029@cluster0.58ggi.mongodb.net/fastapi?retryWrites=true&w=majority")
db = client.fastapi

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

"""
post = {"author": "Mikey",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print(post_id)
"""


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {
        "message": "Hello Heroku",
        "framework": "FastAPI",
    }


@app.get("/sensor/{t}")
async def get_sensor_data(t: float):
    return {"Temperature:": t}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name:": model_name, "message": "LeCNN all the images"}

    return {"model_name:": model_name, "message": "Have some residuals"}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int,
        item_id: str,
        q: Optional[str] = None,
        short: bool = False
):

    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
