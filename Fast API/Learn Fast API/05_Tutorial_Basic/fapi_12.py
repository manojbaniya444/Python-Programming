# When the query is deprecated but still someone are using but want our docs to show it as deprecated we can use depecated property as True

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(
    q: Annotated[
        str ,
        Query(
            alias="item-query",
            title="Query string",
            min_length=3,
            max_length=10,
            description="Query string for the items to search in the database that have a good match",
            deprecated=True,
            include_in_schema=False # not include a query parameter in schema of openAPI documentation
        )
    ]
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results