# Request Body
# when we send data from a client we send in a request body as string

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
class Price(BaseModel):
    price: float
    
app = FastAPI()

@app.post("/items")
async def create_item(item: Item, item_id: int): # this item is the json item that is sent from body of request
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return {"item_id": item_id, **item.model_dump()}

@app.post("/price")
async def create_price(price: Price): # if used pydantic price then it is body price else it is the query parameter price and is required
    return price

@app.post("/users/{user_id}/comment/{comment_id}")
async def all_types_parameter(
    user_id: int, comment_id: str, item: Item, page: int =0
):
    return {"user_id": user_id, "comment_id": comment_id, "item": item, "page": page}