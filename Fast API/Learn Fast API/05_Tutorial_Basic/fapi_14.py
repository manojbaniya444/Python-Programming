from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at" # literal is used to restrict the values to only the ones mentioned
    tags: list[str] = []
    
    # forbid any extra query parameters
    model_config = {
        "extra": "forbid" # i.e if any extra query parameter is passed then it will raise an error
        # https://example.com/items/?limit=10&tool=True error for tool parameter which is extra
    }
    
@app.get("/items/") #{{fastapi}}/items?offset=2&order_by=updated_at&tags=abc&tags=cda
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query.model_dump()