# more metadata

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(
    q: Annotated[str | None, Query(title="Query string",min_length=3, description = "Query string for the items to search in the database that have a good match",)] = None, # this is the query string validation and metadata for the query string
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/alias")
async def alias_query(q: str = Query(alias="item-query")): # can use item-query in the url without getting error
    return {"q": q}