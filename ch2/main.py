from fastapi import FastAPI
from enum import Enum

app = FastAPI()

## order of path parameter matters


@app.get("/products/{product_id}")
async def get_product_reviews(product_id: str):
    return {"message": f"Reviews for product with ID {product_id} retrieved successfully!"}


@app.get("/products/reviews")
async def get_all_reviews():
    
    return {"message": "All reviews retrieved successfully!"}



# default path parameters 

class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME = "home"
    
@app.get("/products/category/{category}")
async def get_products_by_category(category: ProductCategory):
    if category == ProductCategory.ELECTRONICS:
        return {"message": "Products in the 'electronics' category retrieved successfully!"}
    elif category.value == "fashion":
        return {"message": "Products in the 'fashion' category retrieved successfully!"}
    elif category == ProductCategory.HOME.value:
        return {"message": "Products in the 'home' category retrieved successfully!"}
    else:
        return {"message": "Invalid category!"}
    
    # return {"message": f"Products in category '{category}' retrieved successfully!"}