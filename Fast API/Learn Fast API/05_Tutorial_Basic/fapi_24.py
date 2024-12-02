from typing import Annotated

from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.post("/uploadfile")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form(...)]
): # can be multiple file form data but not json together here
    return {
        "file_size": len(file),
        "token": token,
        "file_content_type": fileb.content_type
    }