from fastapi import FastAPI, status , Cookie, Body
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# @app.get("/products/recomendations", status_code=status.HTTP_200_OK)
# async def get_recomendations(session_id : Annotated[str | None , Cookie()]= None):
#     if session_id :
#         return {"session_id" : session_id, "msg" : "Recommending based on cookie"}
#     return {"msg" : "No recommendation"}


# cookie parameter with pydantic model
# class ProductCookie(BaseModel):
#     session_id : str
#     preferred_category : str | None = None
#     tracking_id : str | None = None
    
    
## Forbidding extra cookies
# class ProductCookie(BaseModel):
#     session_id : str
#     preferred_category : str | None = None
#     tracking_id : str | None = None
    
#     model_config = {"extra" : "forbid"}
    
    

# @app.get("/products/recommendations")
# async def get_recommendations(cookies : Annotated[ProductCookie , Cookie()]):

#     # execute through curl because swagger cant execute cookie parameters
#     #curl -X 'GET' 'http://127.0.0.1:8000/products/recommendations' -H 'accept: application/json' -H 'Cookie: session_id=123'

#     response = {"session_id" : cookies.session_id}
        
#     # curl -X 'GET'   'http://127.0.0.1:8000/products/recommendations'   -H 'accept: application/json'   -H 'Cookie: session_id=123' -H 'Cookie: preferred_category=2'
#     if cookies.preferred_category:
#         response["preferred_category"] = cookies.preferred_category


#     # curl -X 'GET'   'http://127.0.0.1:8000/products/recommendations'   -H 'accept: application/json'   -H 'Cookie: session_id=123' -H 'Cookie: preferred_category=2' -H 'Cookie: tracking_id=43434'
#     if cookies.tracking_id:
#         response["tracking_id"] = cookies.tracking_id
        
#     return response
    
    
## Combining with body parameters
class ProductCookie(BaseModel):
    model_config = {"extra":"forbid"}
    session_id : str = Field(title = "Session ID" , 
                             description= "Session id description")
    preferred_category : str | None = Field(default= None, 
                                            title="Preferred Category",
                                            description="Preferred Category Description"
                                            )
class Product(BaseModel):
    min_price : float = Field(ge=0, 
                              title="Minimum price",
                              description= "Minimum price description")
    max_price : float | None = Field(default=None, 
                               ge=10, 
                              title="Minimum price",
                              description= "Minimum price description")
    
@app.post("/products/recomendations")
async def create_product(product : Annotated[Product, Body(embed=True)], 
                         cookies : Annotated[ProductCookie, Cookie()]):
    
    """               
    curl -X 'POST' \
    'http://127.0.0.1:8000/products/recomendations' \
    -H 'accept: application/json' \
    -H 'Cookie: session_id=hello' \
    -H 'Content-Type: application/json' \
    -d '{
    "product": {
        "min_price": 0,
        "max_price": 10
    }
    }'

    """

    
    response = {"session_id" : cookies.session_id}
    """               
    curl -X 'POST' \
    'http://127.0.0.1:8000/products/recomendations' \
    -H 'accept: application/json' \
    -H 'Cookie: session_id=hello' \
    -H 'Cookie: preferred_category=car' \
    -H 'Content-Type: application/json' \
    -d '{
    "product": {
        "min_price": 0,
        "max_price": 10
    }
    }'

    """
    if cookies.preferred_category:
        response["preferred_category"] =  cookies.preferred_category

    response["price_range"] = {
        "min_price" : product.min_price,
        "max_price" : product.max_price
    }
    return response
        