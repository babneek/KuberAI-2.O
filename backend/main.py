from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from model import get_llm_response
from database import save_investment
import sqlite3

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not found in environment variables.")

# Initialize FastAPI app
app = FastAPI()

# Request schema
class ChatRequest(BaseModel):
    query: str

# Response schema
class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    print(f"Received query: {request.query}")  # <-- Add this line
    try:
        answer = get_llm_response(request.query)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class Purchase(BaseModel):
    username: str
    amount: float
    gold_price: float
    weight: float
    date_time: str

@app.post("/save_purchase")
async def save_purchase(purchase: Purchase):
    try:
        conn = sqlite3.connect("data/purchases.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                amount REAL,
                gold_price REAL,
                weight REAL,
                date_time TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO purchases (username, amount, gold_price, weight, date_time)
            VALUES (?, ?, ?, ?, ?)
        """, (purchase.username, purchase.amount, purchase.gold_price, purchase.weight, purchase.date_time))
        conn.commit()
        conn.close()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/invest")
async def invest(request: Request):
    data = await request.json()
    username = data.get("username")
    amount = data.get("amount")
    gold_price = data.get("gold_price")
    weight = data.get("weight")
    success = save_investment(username, amount, gold_price, weight)
    return {"status": "success" if success else "error"}
