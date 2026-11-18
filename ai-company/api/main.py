import os
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from agents.sales import reply_to

app = FastAPI()

class Msg(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/sales")
def sales(msg: Msg, x_api_key: str = Header(None)):
    if x_api_key != os.environ.get("API_SECRET"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"reply": reply_to(msg.text)}