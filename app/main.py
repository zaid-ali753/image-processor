# app/main.py
from fastapi import FastAPI
from app.api.endpoints.router import router 
from app.db.database import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(router, prefix="/image", tags=["image"])
