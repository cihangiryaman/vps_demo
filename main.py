from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    name: str

class ResponseBody(BaseModel):
    message: str

@app.post("/")
async def root(item: RequestBody):
    return ResponseBody(message=f"Hello {item.name}")