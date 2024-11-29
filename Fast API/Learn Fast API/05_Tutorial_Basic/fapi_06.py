# multiple path parameters and multiple query parameters at the same time

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id/items{item_id}}")
async def user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"user_id": user_id, "item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item