# Regex

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(
    query: Annotated[str | None, Query(min_length=3, max_length=10, pattern=r"^fixedquery$")] = None, # this pattern does not allow any other query string except "fixedquery",
    required_query: Annotated[str, Query(min_length=3)] = ...
):
    if query:
        return {"query": query, "required_query": required_query}
    return {"query": "No query provided"}

@app.get("/items2")
async def get_list_items(query: Annotated[list[str], Query()] = None): # if we dont specify the Query() then the list is expected from the body so specifying Query() allow the fastapi to expect the list from the query string as: ?query=one&query=two
    return {"query": query}