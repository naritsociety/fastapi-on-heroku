## FastAPI on heroku

[Tutorial Web](https://www.tutlinks.com/create-and-deploy-fastapi-app-to-heroku/)
```
pip install fastapi
```
```
pip install uvicorn
```
```
pip install gunicorn
```
```
pip freeze > requirements.txt
```
```
pip install -r requirements.txt
```
```
uvicorn --port 5000 --host 127.0.0.1 main:app --reload
```

## Create Procfile
```
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```