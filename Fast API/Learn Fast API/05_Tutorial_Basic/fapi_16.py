# multiple body parameters
from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    
class User(BaseModel):
    username: str
    full_name: str
    
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The id of the item to update", ge=1, le=100, example=10)], # path parameter
    q: str, # query optional parameter
    item: Item, # body json
    user: User, # body json
    importance: Annotated[int, Body()] # since it is a single parameter and might be a query so we specify Body() to make it a body parameter
): 
# { # expected body in json
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }
    results = {"item_id": item_id, "q": q, "user": user, "importance": importance}
    if q:
        results.update({"q": q, "user": user})
    if item:
        results.update({"item": item, "user": user})
    
    return results