# Cookie parameter
from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Cookies(BaseModel):
    model_config = {"extra": "forbid"}
    ads_id: str
    name: str

@app.get("/users")
async def read_users(
    ads_id: Annotated[str | None, Cookie()] = "123cookie12",
    name: str = Cookie(default=None, min_length=2)
):
    return {"ads_id": ads_id, "name": name}

@app.get("/cookies")
async def get_cookies(
    cookies: Annotated[Cookies, Cookie()]
):
    if cookies:
        return True
    else:
        return None