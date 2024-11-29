# path parameter

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello welcome" # content type is application/json by default

@app.get("/products/1") # if the route is /products/1 then we get this function first
async def get_item1():
    return {"item": "1"}

@app.get("/products/{product_id}")
async def get_product(product_id: int): # use this so automatically it will validate for use automatically
    
    # parameter should be same as path parameter
    # If we send any string in place of integer then response will throw error if we had used int as type
    # datavalidation is done by pydantic under the hood so we just have to specify type for the parameter.
    
    return {"product_id": product_id}