from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Multiple Body parameters validation using pydantic


class Product(BaseModel):
    name : str
    price : float
    stock : int | None  = None

    
class Seller(BaseModel):
    username : str
    full_name :str | None = None

# @app.post("/products")
# async def create_product(product : Product, seller : Seller):
#     return {"product" : product, "seller"  : seller}


# Make body optional 

# @app.post("/products")
# async def create_product(product : Product, seller : Seller | None = None):
#     return {"product" : product, "seller"  : seller}


# Add a new key from body (singular keys)
# @app.post("/products")
# async def create_product(product : Product, seller : Seller , sec_key: Annotated[str, Body()]):
#     return {"product" : product, "seller"  : seller, "sec_key" : sec_key}
    
# Without Embed

"""
body = {
"name": "string",
"price": 0,
"stock": 0
}

"""
@app.post("/products")
async def create_product(product : Product):
    return product


# With Embed

"""
body = {
  "product": {
    "name": "string",
    "price": 0,
    "stock": 0
  }
}
"""
@app.post("/products")
async def create_product(product : Annotated[Product, Body(embed=True)]):
    return product