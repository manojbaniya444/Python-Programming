# Response Model
from typing import Any

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class UserLogin(BaseModel):
    username: str
    password: str
    email: str
    full_name: str
    
class UserLoginResponse(BaseModel):
    username: str
    email: str

class UserEmailView(UserLoginResponse):
    password: str
    
# we user response model to filter out the response so that it dont contain password for security
@app.post("/login", response_model=UserLoginResponse, status_code=201)
async def login(user: UserLogin):
    return user

@app.post("/email")
async def email(user: UserEmailView) -> UserLoginResponse:
    return user

@app.get("/response")
async def response(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.google.com")
    else:
        return JSONResponse(
            content={
                "message": "Hello world"
            }
        )
        
@app.get("/response2", response_model=None) # disable response model to disable all its features for now to allow our custom behaviour like Response | dict
async def response2(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.google.com")
    else:
        response = {
            "message": "Hello world",
            "data": [1,2,3,4,5,6,7,8]
        }
        return response