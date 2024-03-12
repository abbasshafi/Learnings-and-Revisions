from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class Hello(BaseModel):
#     name: str
#     age: int

@app.get('/')
async def msg():
    return "Asalamulaikum!"

@app.get('/{name}')
async def msg(name:str):
    if name == "abbas":
        return "aji senga chal de"
    elif name == "Majid":
        return "qarayyy senga chal de"
    elif name == "Nomi":
        return "da Engineer zuma senga chal de"
    
    else:
        return "Hello mate"
    
