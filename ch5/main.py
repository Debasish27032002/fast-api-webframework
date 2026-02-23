# Validation in query ro path parameters
from fastapi import FastAPI , Query
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
        }
    ]

# @app.get("/products/")
# async def get_all_products(search : str | None = None):
#     if search:
#         filtered_products = [product for product in PRODUCTS if search.lower() in product["name"].lower()]
#         return filtered_products
#     return PRODUCTS



# OLD way of doing validation in query parameters
# @app.get("/products/")
# async def get_all_products(search : str | None = Query(default = None, min_length=2, max_length=5)):
#     if search:
#         filtered_products = [product for product in PRODUCTS if search.lower() in product["name"].lower()]
#         return filtered_products
#     return PRODUCTS

# @app.get("/products/")
# async def get_all_products(search : Annotated[str | None, Query( min_length=2, max_length=5)] = None):
#     if search:
#         filtered_products = [product for product in PRODUCTS if search.lower() in product["name"].lower()]
#         return filtered_products
#     return PRODUCTS



# @app.get("/products/all")
# async def get_all_products(search : Annotated[str | None, Query( min_length=2, max_length=5 , pattern= "^[a-z]*$")] = None):
#     if search:
#         filtered_products = [product for product in PRODUCTS if search.lower() in product["name"].lower()]
#         return filtered_products
#     return PRODUCTS


# MULTIPLE SEARCH PARAMETERS

@app.get("/products")
async def get_products(search : Annotated[ list[str] | None , Query(min_length=2, max_length=5)] = None):
    if search:
        filtered_products = [product for product in PRODUCTS if any(s.lower() in product["name"].lower() for s in search)]
        return filtered_products
    return PRODUCTS

