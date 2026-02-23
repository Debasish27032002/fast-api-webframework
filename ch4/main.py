from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# path converter 

# @app.get("/products")
# async def get_product_reviews(product_id: str):
#     return {"message": f"Reviews for product with ID {product_id} retrieved successfully!"}

# @app.get("/products/{id}")
# async def get_product(id:str, category: str):
#     return {"message": f"Product with ID {id} in category {category} retrieved successfully!"}

# @app.get("/products/{id}")
# async def get_product(id:str, category: str | None = None):
#     return {"message": f"Product with ID {id} in category {category} retrieved successfully!"}


@app.get("/products/{id}")
async def get_product(id:str, category: str | None = None, limit : int = 10):
    return {"product_id": id, "category": category, "limit": limit}

