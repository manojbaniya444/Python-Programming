# Header value
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/users")
async def read_users(
    user_agent: Annotated[str | None, Header()] = None,
):
    if user_agent:
        return True
    else:
        return "false"