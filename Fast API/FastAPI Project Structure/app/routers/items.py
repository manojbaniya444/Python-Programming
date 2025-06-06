from fastapi import APIRouter, Depends, HTTPException

from ..dependency import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {
    "plumbus": {"name": "Plumbus"},
    "gun": {"name": "Portal Gun"},
}

@router.get("/")
async def read_items():
    return "Hello world"

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item_id": item_id, "name": fake_items_db[item_id]["name"]}
    
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation Forbidden"}}
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}