from fastapi import Depends, FastAPI

from .dependency import get_query_token, get_token_header
from .internal import admin
from .routers import items, users # to avoid the name collision for router we are only importing the main file

app = FastAPI(dependencies=[Depends(get_query_token)])
# app = FastAPI()

app.include_router(users.router) # "/users"
app.include_router(items.router) # "/items"
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I am a teapot"}}
)

@app.get("/")
async def root():
    return {"message": "Hello from the server."}