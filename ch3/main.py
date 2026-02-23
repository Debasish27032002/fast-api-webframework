from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# path converter 

@app.get("/file/{file_path:path}")
async def get_file(file_path: str):
    return {"message": f"File '{file_path}' retrieved successfully!"}