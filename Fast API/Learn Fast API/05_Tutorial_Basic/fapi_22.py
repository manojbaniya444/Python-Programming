# file uploaded by client
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile") # file uploaded as form data abd cibtebt as bytes will be read
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/upload")
async def upload_file(file: UploadFile):
    filecontent = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

@app.post("/multiple_file")
async def multiple_file(files: list[UploadFile] = File(description="Upload multiple files")):
    return {
        "filenames": [file.filename for file in files]
    }
    
# advantage of UploadFile
# - dont have to mention File() to specify it as file from form data in the request
# - a file stored in memory up to a maximum size and then to disk so that it can handle large file
# - we can get metadata from the uploaded file
# - we can use it as a normal file-like object