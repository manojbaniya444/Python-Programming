from fastapi import FastAPI

# initialize the app
app = FastAPI()

# adding our first route
@app.get("/")
def root():
    return {"message": "Hello World"}