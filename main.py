from fastapi import FastAPI
from pymongo import MongoClient
import datetime

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


@app.get("/")
async def root():
    return {
        "message": "Hello Heroku",
        "framework": "FastAPI",
    }


@app.get("/data/{t}")
async def get_sensor_data(t: float):
    return {"Temperature:": t}
