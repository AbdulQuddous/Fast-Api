from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

# @app.get('/')
# def home():
#     return {'message':"Welcome"}

# @app.get('/About')
# def home():
#     return {'message':"Welcome to about"}

# @app.get('/user/{user_id}')
# def home(user_id:int):
#     return {
#         'users':user_id
#     }

# @app.get('/product/')
# def home(name:str=None):
#     return {
#         'users':name
#     }

# @app.get('/item/')
# def home(name:str=None,limit:int=10):
#     return {
#         'name':name , 'limit':limit
#     }
class data(BaseModel):
    name:str
    age:int

@app.post('/user/')
def user_data(user:data):
    return {
        'message':"Welcome",
        'user':user,
    }