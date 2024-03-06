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

@app.get('/blog/{id}')
def show(id):
    return{'id':id}

#if we write int so it only accepts the string routing 
@app.get('/blogs/{id}')
def show2(id:int):
    return{'data':id}

@app.post('/name/{name}')
def name(name:str):
    return {'The name of the client is':name}

##Query Parameter
#if we have 1000 parameters in database we cannot fetch it as it is inefficant
#so we provide query parameter to set a limit how much data i want to fetch
@app.get('/blog?limit=10published=true')
def index():

    return {'data': 'blog list'}