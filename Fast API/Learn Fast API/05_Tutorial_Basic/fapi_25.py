# HTTPException

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    1: {"name": "Foo"},
    2: {"name": "Bar"},
    3: {"name": "Baz"},
}

@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict | HTTPException:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="not found", headers={"X-Error": "There goes my error"})
    return {
        "item": items[item_id]
    }