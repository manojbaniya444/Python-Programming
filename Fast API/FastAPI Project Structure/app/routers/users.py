from fastapi import APIRouter

# like an fastapi class but with feature for the route of api url
router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"username": "fakeuserofme"}

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}