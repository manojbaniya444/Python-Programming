from fastapi import FastAPI, Query
from typing import Union
from typing_extensions import Annotated

app = FastAPI()

@app.get("/items")
async def read_item(query: str | None = None): # query string validation or None (Optional)
    if query:
        return {"query": query}
    return {"query": "No query provided"}

@app.get("/items2")
async def read_items(query: Annotated[Union[str, None], Query(max_length=50)] = None): # query string validation or None (Optional)
    # max_length is the maximum length of the query string
    # instead of Union we could use str | None
    # Query() is for query validation
    if query:
        return {"query": query}
    return {"query": "No query provided"}

# Annotated[str, Query()] = "default"
# str = Query(default="default")
# Advantage of Annotated is that we can add more metadata to the query parameter