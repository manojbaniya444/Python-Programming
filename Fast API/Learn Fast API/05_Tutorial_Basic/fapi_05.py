# Query Parameter

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): # parameter other than path parameter is query parameter
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}") # path parameter item_id
async def get_item(item_id: str, q: str | None = None): # query parameter q optional
    if q:
        return {"item_id": item_id, "q": q}
    else:
        return {"item_id": item_id}
    
@app.get("/foods/{food_id}")
async def get_food(food_id: int, extra: str | None = None, chilly: bool = True): # we can also use the boolean type and it will be converted
    foods = {1: "Pizza", 2: "Burger", 3: "Pasta"}
    if extra:
        return {"food_id": food_id, "food": foods[food_id], "extra": extra}
    if chilly:
        return {"food_id": food_id, "food": foods[food_id], "message": "No chilly"}

# Here we have defined two query parameters skip and limit that goes like "/items/?skip=0&limit=10" in the url