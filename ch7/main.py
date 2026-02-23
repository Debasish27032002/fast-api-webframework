from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# # Basic without any authentication 
# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product:dict):
#     return {"message" : "Product created successfully", "product" : new_product}



# Validation of body with pydantic base model 

# Define a base model with structure
class Product(BaseModel):
    id : int
    name : str
    price : float
    stock : int | None = None
    
# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product : Product):
#     return {"msg" : "New product created successfully" , "product" : new_product}


# ## Access Attribute inside Function
# @app.post("/products/", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product : Product):
#     print(new_product.id, new_product.name, new_product.price )
#     return {"msg" : "New product created successfully" , "product" : new_product}


# Add new calcualted attribut to pydantic base model 

@app.post("/products/")
async def create_product(new_product : Product):
    # product_dict = new_product.dict() # depricated
    product_dict = new_product.model_dump()
    product_dict["price_after_tax"]  = product_dict["price"] + 0.18*new_product.price
    return {"msg" : "New product created succesfully" , "product" : product_dict}


# Add path parameter to request payload

# @app.put("/products/{product_id}", status_code= status.HTTP_200_OK)
# async def update_product(product_id : int, new_product_data : Product):
#     return {"new_product_data" : new_product_data, "product_id" : product_id}

# Add query parameter with request payload and path parameter
@app.put("/products/{product_id}", status_code= status.HTTP_200_OK)
async def update_product(product_id : int, new_product_data : Product, discount : float| None = None):
    return {"new_product_data" : new_product_data, "product_id" : product_id, "discount" : discount}


