## Fast API tutorial
This contains begineer Fast API tutorial.

A simple api with route "/" GET method.
```python
# create a simple api
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): # can use async or normal
    return {"message": "Hello World"}
```
Run the app with `fastapi dev main.py` usin g`fastapi` CLI tool need to install.

Now the app should run in `localhost:8000` by default.

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
- [Multiple Path and Query Parameter](./fapi_06.py)
- [Optional Query Parameter and Required Query Parameter](./fapi_07.py)
- [Request Body Pydantic](./fapi_08.py)
- [Query String Validation](./fapi_09.py)
- [Multiple Query Parameter](./fapi_10.py)
- [More Metadata in Query](./fapi_11.py)
- [Deprecating Parameters](./fapi_12.py)
- [Path Parameter Validationn](./fapi_13.py)
- [Pydantic Model for Queries](./fapi_15.py)
- [Nested Body JSON](./fapi_17.py)
- [Reading Cookie values](./fapi_18.py)
- [Reading Header values](./fapi_19.py)
- [Response Model](./fapi_20.py)
- [Form Data](./fapi_21.py)
- [File](./fapi_22.py)
- [File and Form](./fapi_24.py)
- [HTTP Exception](./fapi_25.py)
- [CORS](./fapi_26.py)
- [security OAuth](./fapi_27.py)