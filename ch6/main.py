from fastapi import FastAPI, Path, Query, status
from typing import Annotated

app = FastAPI()

PRODUCTS = [
    {
        "id" : 1,
        "name" : "Laptop",
        "price" : 999.99,
        "description" : "A high-performance laptop for work and play."
    },
    {
        "id" : 2,
        "name" : "Smartphone",
        "price" : 499.99,       
        "description" : "A sleek smartphone with a powerful camera."
    },
    {
        "id" : 3,
        "name" : "Headphones",
        "price" : 199.99,       
        "description" : "Noise-cancelling headphones for immersive sound."
    }
]


# # Basic  path parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id:int):
#     return [product for product in PRODUCTS if product["id"] == product_id]


@app.get("/products/{product_id}", status_code=status.HTTP_302_FOUND)
async def get_product(product_id:Annotated[int , Path(ge=1)],
                      search : Annotated[str | None, Query(max_length=5)] = None):
    if search:
        return [product for product in PRODUCTS if search.lower() in product["name"].lower()]
    return [product for product in PRODUCTS if product["id"] == product_id]