#first install:
# pip install fastapi
# pip install uvicorn

from fastapi import FastAPI
import uvicorn

app= FastAPI()

@app.get("/")
def index():
    return "welcome"


#when ever we will be calling this api Welcome it will expects an input as string
@app.get('/Welcome')
def get_name(name:str):
     return {'Happy Learning FASTAPI': f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)



#to run the file:
# uvicorn main:app --reload



