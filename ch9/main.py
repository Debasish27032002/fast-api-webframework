from fastapi import FastAPI, status
from pydantic import BaseModel, Field


app = FastAPI()


# Add validations inside fields of models using Field() function of pydantic. It allows us to add validations like max_length, min_length, ge, le, pattern etc. We can also add title and description for better documentation of our API.
class Product(BaseModel):
    name : str = Field(max_length=10, pattern="^[A-Za-z0-9]+$",
                       title = "Product name" ,
                       description= "Name of the product")
    price : float = Field(ge = 1,
                          title = "Product Price",
                          description= "Price of the product in float greater than 0")
    stock : float | None = Field(default= None, 
                                 title = "Stock",
                                 description="Stock of product")
    
    


@app.post("/products", status_code = status.HTTP_200_OK)
async def create_product(product : Product):
    return {"msg" : "New product data" , "product" : product}


