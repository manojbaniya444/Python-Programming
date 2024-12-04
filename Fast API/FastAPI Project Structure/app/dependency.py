"""contain dependecy that will be used in several part of the application"""

from fastapi import Header, HTTPException
from typing_extensions import Annotated

async def get_token_header(x_token: Annotated[str, Header()]): # here variable is x_token but header should be x-token hai
    if x_token != "fake-super-secret-token":
        raise HTTPException(
            status_code=400,
            detail="X-Token header invalid"
        )
        
async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=400,
            detail="No Jessica token provided"
        )