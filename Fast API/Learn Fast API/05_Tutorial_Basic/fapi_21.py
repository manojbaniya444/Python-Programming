# form data get
from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class UserDetails(BaseModel):
    name: str
    email: str
    age: int
    model_config = {
        "extra": "forbid"
    }
    
@app.post("/user")
async def user(user: Annotated[UserDetails, Form()]):
    return user