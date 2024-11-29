# Required query parameter: If we dont want to add a specific value but just want to make it optional, set the default to None

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, required: int,  needy: str | None = None): # if needy is not provided, it will be None else string is needed
    item = {"item_id": item_id, "needy": needy}
    return item