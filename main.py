from fastapi import FastAPI
from pymongo import MongoClient
from enum import Enum
# import datetime

app = FastAPI()

client = MongoClient("mongodb+srv://narit:Crazydog2029@cluster0.58ggi.mongodb.net/fastapi?retryWrites=true&w=majority")
db = client.fastapi

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