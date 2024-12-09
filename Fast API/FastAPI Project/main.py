from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    order_id: int
    order_name: str

# root url
@app.get("/")
async def hello():
    return {"message": "Hello world"}

# using query path and default parameter together with gender parameter optional
@app.get("/greet/{name}")
async def greet_with_name(name: str, age: int, gender: str = "Unknown") -> str:
    return f"Hello {name} welcome to FastAPI server with age {age} and gender {gender}"

# making post request
@app.post("/create_order")
async def create_order(order: Order):
    return {"message": "Order created successfully", "order": order}