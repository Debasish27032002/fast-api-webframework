from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any, Optional

app = FastAPI()

class Product(BaseModel):
  id: int
  name: str
  price : float
  stock: int | None = None

class ProductOut(BaseModel):
  name: str
  price : float

## without response_model Parameter
# @app.get("/products/")
# async def get_products():
#   return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}

# with response_model Parameter
@app.get("/products/", response_model=Product)
async def get_products():
  return {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5}


# @app.get("/products/", response_model=List[Product])
# async def get_products():
#   return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7}
#     ]

# @app.get("/products/", response_model=List[Product])
# async def get_products():
#   return [
#        {"id": 1, "name": "Moto E", "price": 33.44, "stock": 5, "description": "Hello Desc1"},
#        {"id": 2, "name": "Redmi 4", "price": 55.33, "stock": 7, "description": "Hello Desc2"}
#     ]

# @app.post("/products/", response_model=Product)
# async def create_product(product: Product):
#   return product

# class BaseUser(BaseModel):
#     username: str
#     full_name: str | None = None

# class UserIn(BaseUser):
#     password: str

# @app.post("/users/", response_model=BaseUser)
# async def create_user(user: UserIn):
#   return user

# @app.post("/products/", response_model=Product)
# async def create_product(product: Product) -> Any:
#   return product

# @app.post("/products/", response_model=None)
# async def create_product(product: Product) -> Any:
#   return product




## Excluding Unset Default Values

products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "stock": 10, "is_active": True},
    "2": {"id": "2", "name": "Smartphone", "price": 499.99, "stock": 50, "is_active": False}
}

class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    tax: float = 15.0  # Default tax rate

@app.get("/products/{product_id}", response_model=Product, response_model_exclude_unset=True)
async def get_product(product_id: str):
    return products_db.get(product_id, {})

## Including Specific Fields
# @app.get("/products/{product_id}", response_model=Product, response_model_include={"name", "price"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})

# ## Excluding Specific Fields
# @app.get("/products/{product_id}", response_model=Product, response_model_exclude={"tax", "description"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})