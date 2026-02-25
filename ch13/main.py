from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()


# Header parameter
# curl -X 'GET'   'http://127.0.0.1:8000/products'   -H 'accept: application/json'   -H 'header: 112' 


# @app.get("/products")
# async def get_products(header : Annotated[str | None , Header()] = None):
#     return {"header" : header }


# Duplicate headers
# curl -X 'GET'   'http://127.0.0.1:8000/products'   -H 'accept: application/json'   -H 'header: 112' -H 'header: here'
# @app.get("/products")
# async def get_products(header : Annotated[list[str] | None , Header()] = None):
#     return {"headers" : header}


class ProductHeader(BaseModel):
    authorization  : str
    accept_language : str | None = None
    x_tracking_id : list[str] = []
    
    
    # if you want to forbid any extra headers
    
    model_config = {"extra" : "forbid"}
    
#  curl -X 'GET'   'http://127.0.0.1:8000/products'   -H 'accept: application/json'   -H 'authorization: Bearer token123' -H 'accept_language: eng' -H 'x_tracking_id : track1' -H 'x_tracking_id : track2'

@app.get("/products")
async def get_products(headers : Annotated[ProductHeader , Header()]):
    return {"headers" : headers}


# We can combine header parameter with cookie paramater and body if we want the same way by builind different pydantic model