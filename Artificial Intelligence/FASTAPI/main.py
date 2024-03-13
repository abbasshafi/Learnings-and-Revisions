from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def abc():
    return "Hey!"

@app.get('/abbas')
def ghi():
    return "Hey! My name is Abbas"

##Path Parameters
#for dynamic routing use the {}
#/users/{user_id} where user_id is a path parameter that captures a specific user's ID.

@app.get('/blog/{id}')
def show(id):
    return{'id':id}

#if we write int so it only accepts the string routing 
@app.get('/blogs/{id}')
def show2(id:int):
    return{'data':id}

@app.get('/name/{name}')
def name(name:str):
    return {'The name of the client is':name}

##Query Parameter
#if we have 1000 parameters in database we cannot fetch it as it is inefficant
#so we provide query parameter to set a limit how much data i want to fetch
#Use query parameters for optional filtering, sorting and selecting 
@app.get('/blog?limit=10published=true')
def index():

    return {'data': 'blog list'}

##Request body
#The request body contains the data that the client wants to send to the server.
from pydantic import BaseModel
class signup(BaseModel):
    first_name:str
    last_name:str
    age:int


@app.post('/signup')
def signup(Signup:signup):
    return {'data':f"Account created successfully for user {Signup.first_name}"}


##create folder:
# -create __init__.py file
# -then make a requirement.txt file
# to execute the requirement file run command "pip3 install -r requirements.txt"
# -create a virtual enviroment using command "python3 -m venv Signup Form-env"
# mian.py containing the main code 
#create schemas.py and cut paste the pydantic class into the file
# then write from . import schemas into main.py file
# and mention the schemas in the function parameters


##Database Connection
First create database.py File 
then write these lines of code in the file 
"from sqlalchemy import create_engine"
then create signup.db File
and create the command in the database.py File
"engine=create_engine('sqlite:// name of databasefile.db, echo=True')"
