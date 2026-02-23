from fastapi import FastAPI

app = FastAPI()


# Get request
# read or fetch all data
@app.get("/products")
async def get_all_products():
    return {"message": "All products retrieved successfully!"}


@app.get("/products/{product_id}")
async def get_product(product_id : int) :
    return {"message": f"Product with ID {product_id} retrieved successfully!"}

@app.post("/products")
async def create_product(new_product: dict):
    return {"message": "Product created successfully!" , "product": new_product}

# complete data update
@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: dict):
    return {"message": f"Product with ID {product_id} updated successfully!" , "updated_product": updated_product}

# partial data update
@app.patch("/products/{product_id}")
async def partial_update_product(product_id: int, updated_fields: dict):
    return {"message": f"Product with ID {product_id} partially updated successfully!" , "updated_fields": updated_fields}

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return {"message": f"Product with ID {product_id} deleted successfully!"}

## order of path parameter matters

@app.get("/products/{product_id}")
async def get_product_reviews(product_id: int):
    return {"message": f"Reviews for product with ID {product_id} retrieved successfully!"}

@app.get("/products/reviews")
async def get_all_reviews():
    return {"message": "All reviews retrieved successfully!"}