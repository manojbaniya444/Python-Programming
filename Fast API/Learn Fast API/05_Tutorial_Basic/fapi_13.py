# Path Parameter Validation

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def get_items(
    item_id: Annotated[
        int, Path(
            title="The id of the item to get",
            ge=1, # greater than or equal to 1
            le=10 # less than or equal to 10
        )
    ], # validation for path parameter
    size: Annotated[float, Query(gt=1.0, le=10.0)],
    q: Annotated[str | None, Query(alias="item-query")] = "default", # validation for query parameter
    
):
    return {"item_id": item_id, "size": size, "q": q}