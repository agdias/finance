from fastapi import FastAPI

from app.routers import stocks

app = FastAPI()

app.include_router(stocks.router)
