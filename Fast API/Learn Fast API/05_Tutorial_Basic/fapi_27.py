# Security

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

def fake_hash_password(password: str):
    return "fakehashed" + password

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # "/token" is the url where the user send to get the token

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None
    
class UserInDB(User):
    hashed_password: str
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    
def fake_decode_token(token):
    # verify token here
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return user
    
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="User Inactive")
    return current_user

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

# form with username password
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400, detail="Incorrect Password"
        )
    return {
        "access_token": user.username, "token_type": "bearer",
    }

@app.get("/users/me")
async def read_users_me(
    user: Annotated[User, Depends(get_current_active_user)]
):
    return user

# OAuth2 was designed so that the backend or API could be independent of the server that authenticates user
# 1. User types username and password and hits login button to a url "/token"
# 2. THe server checks that username and password and responds with a "token"
# 3. The user will also send the token along with the request that he needs to authenticate to use the API resource.
# 4. Further hashing can be done with other jwt libraries to use in production 
# 5. This is the basic auth flow in fastapi