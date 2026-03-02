from fastapi import FastAPI, Form 
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()


# form for html response

# Encoding in form data - application/x-www-form-urlencoded
# Encoding for file upload - multipart/form-data

# handle form api 
@app.get("/", response_class=HTMLResponse)
async def get_form():
    html_content = """
    <html>
        <head>
            <title>Form Example</title>
        </head>
        <body>
            <h1>Submit Your Name</h1>
            <form action="/submit_with_model" method="post">
                <input type="text" name="name" placeholder="Enter your name" required>
                <input type="number" name="age" placeholder="Enter your age" required>
     # EXtra field - will give error           <input type="text" name="email" placeholder="Enter your email" required>
                <button type="submit">Submit</button>
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/submit")
async def submit_form(name: Annotated[str, Form(min_length=1, max_length=50)]):
    return {"message": f"Hello, {name}!"}


# Form field with pydantic model validation
class FormData(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field( gt=0, lt=120)
    
    model_config = {"extra": "forbid"}


@app.post("/submit_with_model")
async def submit_form_with_model(form_data: Annotated[FormData, Form()]):
    return {"message": f"Hello, {form_data.name}! You are {form_data.age} years old."}

