# FastAPI Project Structure
```
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   │   └── users.py     # "users" submodule, e.g. import app.routers.users
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
```

# APIRouter
APIRouter to manage more routes in our url of the api.

# Testing the route with the PostMan

### **Route: "/"**
This route need the dependency `query token` because we have that dependency in our **main.py** file at the root app.

The url required will be : `url?token=jessica`

Basically the query token is needed by every route to access the api.
```python
# the response will look like
{
    "message": "Hello from the server."
}
```

### **Route: "/users"**
This will also need the dependency `query token` because we have set the dependency required at the top level.

```python
[
    {
        "username": "Rick"
    },
    {
        "username": "Morty"
    }
]
```

Then `/users/me` and `/users/{username}` both will work given the query token.
```python
{
    "username": "fakeuserofme"
}
```

### Route: **"/items"**
In order to access items route we first need `query token` and `header token` both because we have query token dependency set in the main.py app and then header token x-token required set in the items dependency. If any other dependency set in the individual route level by `@decorator` then we will need that dependency too.

Request: `/items/item_name?token=jessica` and Header `x-token: value`.

```python
{
    "message": "Updating admin"
}
```