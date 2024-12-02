from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class UpdatingItem(BaseModel):
    variant: str
    store: str
    website: HttpUrl

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="description",
        max_length=3
    ),
    price: float
    tax: float | None = None
    udating_item: list[UpdatingItem] | None
    
class AllItem(BaseModel):
    item: Item | None = None
    user: str
    
@app.put("/items/{id}")
async def update(
    id: int,
    item: Annotated[Item, Body(embed=True)], # expected in json body as key
):
    results = {
        "item_id": id,
        "item": item.model_dump()
    }
    return results

@app.post("/items/")
async def all(item: AllItem | None):
    if item:
        return item.model_dump()
    else:
        return None