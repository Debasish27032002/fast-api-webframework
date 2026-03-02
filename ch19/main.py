from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

s = {"a" : "hello" , "b" : "Bye"}

# add httpexception and custom header 
@app.get("/item/{item_id}")
async def get_items(item_id : str):
    if item_id in s:
        return s[item_id]
    else:
        raise HTTPException(status_code=404, detail= "Item not found", headers={"x-error-type" : "Item missing"})



# Create Exception
class FruitException(Exception):
    def __init__(self, fruit_name : str):
        self.fruit_name = fruit_name

# Custom Exception handler 
@app.exception_handler(FruitException)
async def fruit_exception_handler(request : Request, exc : FruitException):
    return JSONResponse({"msg" : f"Invalid fruit {exc.fruit_name}"}, status_code=418)


@app.get("/fruits/{fruit_name}")
async def get_fruit(fruit_name : str):
    if fruit_name not in s:
        raise FruitException(fruit_name)
    return s[fruit_name]



from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

# Change default errror handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request : Request, exc : RequestValidationError):
    # return JSONResponse({"msg" : "Custom validation error", "details" : exc.errors()}, status_code=422)
    return PlainTextResponse(str(exc), status_code=422)

@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id" : item_id}    