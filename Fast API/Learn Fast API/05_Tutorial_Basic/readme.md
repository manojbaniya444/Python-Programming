## Fast API tutorial
This contains begineer Fast API tutorial.

```python
# create a simple api
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): # can use async or normal
    return {"message": "Hello World"}
```
Run the app with `fastapi dev main.py` usin g`fastapi` CLI tool.

Now the app should run in `localhost:8000`.

We can see API docs in `http://localhost:8000/docs`

We can see alternative doc in `http://localhost:8000/redoc`

We can see json schema of our openapi in `http://localhost:8080/openapi.json`

## Tutorial code
ALl the code file with link to the source file
- [Creating a simple API with get method](./fapi_01.py)
- [Path Parameter](./fapi_02.py)
- [Enum for predefined values](./fapi_03.py)
- [Catch all path parameter](./fapi_04.py)
- [Query Paramter](./fapi_05.py)