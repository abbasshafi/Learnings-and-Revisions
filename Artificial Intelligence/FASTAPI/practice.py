from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Hello(BaseModel):
    name: str
    age: int

@app.get('/')
async def msg():
    return "Asalamulaikum!"

@app.get('/{name}')
async def msg(name:str):
    return f"Hello Muhtaram {name}!"
