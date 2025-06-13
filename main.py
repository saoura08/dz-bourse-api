from fastapi import FastAPI
from scraper import get_stock_data
from typing import List, Dict

app = FastAPI(title="DZ Bourse API")

@app.get("/")
def root():
    return {"message": "مرحبا بك في DZ Bourse API! استعمل /api/stocks لعرض بيانات الأسهم."}

@app.get("/api/stocks", response_model=List[Dict[str, str]])
def read_stocks():
    return get_stock_data()
