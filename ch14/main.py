from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI()

class Product(BaseModel):
    id : int 
    name : str
    price : float 
    stock : int | None = None


# without retrun type 
@app.get("/products") 
async def get_products():
    return {"status" :"ok"}


# with return type annotations
@app.get("/products/return")
async def get_product_with_return_type() -> Product: # this will give internal server error if we dont return in the way pydantic model
    return {
        "id" : 1,
        "name" : "dafa",
        "price" : 12123.3232,
        "stock"  : 123
    }
    
# return with extra key
@app.get("/products/return/extra")
async def get_product_with_return_type() -> Product: # this will give internal server error if we dont return in the way pydantic model
    return {
        "id" : 1,
        "name" : "dafa",
        "price" : 12123.3232,
        "stock"  : 123,
        "description"  : 'this is extra'

    }
# even if we give extra key which is not in pydantic model this will return only those keys which are in the pydantic model 

    """
    output  = {
  "id": 1,
  "name": "dafa",
  "price": 12123.3232,
  "stock": 123
}
    
    """
    
    
# return list of products - with return type 
@app.get("/products/return/list")
async def get_list_of_products() -> List[Product]:
    return [
        {
        "id" : 1,
        "name" : "dafa",
        "price" : 12123.3232,
        "stock"  : 123,
        "description"  : 'this is extra'

    },
        {
        "id" : 2,
        "name" : "hello",
        "price" : 23.3232,
        "stock"  : 21,

    }
    ]
    
    
# @app.post("/products")
# async def create_product(product_data: Product) -> Product:
#     new_product_data = product_data.model_dump()
#     # del new_product_data["id"] # this will give error as we are deleting a mandatory key from pydantic model 
#     return new_product_data
 

class ProductOut(BaseModel):
    name : str
    price : float
    
    
# this will only return product out parameters which is price and name only 
@app.post("/products")
async def create_product(product_data: Product) -> ProductOut:  
    
    return product_data

class BaseUser(BaseModel):
    username : str
    full_name : str

class UserIn(BaseUser): # we are inheriting the base user here  - so no need to inherit base modle here
    password: str
    

@app.post("/user")
async def create_user(user_data : UserIn) -> BaseUser:
    return user_data

    