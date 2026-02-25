from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()



# Create custom example for proper documentation

# Using field level examples
# class Product(BaseModel):
#     name : str  = Field(examples=["earphones"])
#     price : float = Field(examples=[13.33])
#     stock : int | None = Field(default= None, examples=[10])


# Using pydantic's json_schema_extra

class Product(BaseModel):
    name : str
    price : float
    stock : int | None = None
    
    model_config = {
         "json_schema_extra" : {
            "examples" : [
                {
                    "name" : "Headphones",
                    "price" : 10.1111,
                    "stock" : 99
                }
            ]
        }
    }
    
    
       


@app.post("/products", status_code=status.HTTP_200_OK)
async def create_product(new_product : Product):
    return new_product