from fastapi import FastAPI
from fastapi import Form
#first install python-multipart

app=FastAPI()

@app.post('/forms/data')
async def form_data(username: str= Form(),password:str=Form()):
    return ({"username":username, "password":password})


@app.post('/')
def login(username:str=Form(),password:str=Form()):
    return {"username":username, "password":password}