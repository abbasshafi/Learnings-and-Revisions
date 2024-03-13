from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Hello(BaseModel):
    name: str
    location: str

@app.get('/')
async def msg():
    return "Asalamulaikum!"

@app.get('/{name}')
async def msg(name:str):
    if name == "abbas":
        return f"{name} senga chal de"
    elif name == "Majid":
        return "qarayyy senga chal de"
    elif name == "Nomi":
        return "da Engineer zuma senga chal de"
    
    else:
        return "Hello mate"
    
@app.post('/people/hi')
async def display(HelloC:Hello):
    return HelloC

