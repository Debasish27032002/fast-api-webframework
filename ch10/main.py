from fastapi import FastAPI, status
from pydantic import BaseModel, Field


app = FastAPI()


# Sub model
class Category(BaseModel):
    name : str = Field(max_length= 10, 
                       min_length=1,
                       title="Category Name",
                       description="Name of category")
    
    description : str |None = Field(default=None, 
                                    title = "Category description",
                                    description="Description of Category",
                                    max_length= 100)
    
    
# Main model which will use submodel
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
    
    # category : Category | None = Field(default=None,           # For single category
    #                                    title="Product Category",
    #                                    description="Category to which the product belongs")
    
    
    category : list[Category] | None = Field(default=None,           # For multiple categories in list
                                       title="Product Category",
                                       description="Category to which the product belongs")

@app.post("/products", status_code=status.HTTP_200_OK)
async def create_product(new_product : Product):
    return new_product
    