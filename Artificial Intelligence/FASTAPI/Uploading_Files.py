from fastapi import FastAPI, File, UploadFile


app=FastAPI()

@app.post('/file/upload')
async def fileU(file : bytes=File()):
    return ({"files": len(file)})

@app.post('/file/upload')
def file(file: bytes=File()):
    return ({"files": len(file)})

#returns all information about the file uploaded 
@app.post('/upload/file')
def filesInfo(file: UploadFile):
    return ({"file": file})