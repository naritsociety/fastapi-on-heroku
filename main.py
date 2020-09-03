from fastapi import FastAPI
from pymongo import MongoClient
import datetime

app = FastAPI()

client = MongoClient("mongodb+srv://narit:Crazydog2029@cluster0.58ggi.mongodb.net/fastapi?retryWrites=true&w=majority")
db = client.fastapi

post = {"author": "Mikey",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

@app.get("/")
def hello():
    return {
        "message": "Hello Heroku",
        "framework": "FastAPI",
        "post_id": post_id
    }
