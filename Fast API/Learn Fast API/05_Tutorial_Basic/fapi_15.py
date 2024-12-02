# pydantic model
from typing import Annotated, Lieral

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"} # dont accept any other parameters other than mentioned in the model
    limit: int = Field(100, ge=1, le=1000)
    offset: int = Field(0, ge=0)
    q: str = Query(None, min_length=3, max_length=50)
    tags: list[str]
    
@app.get("/items/")
async def read_items(filter_params: FilterParams):
    return filter_params