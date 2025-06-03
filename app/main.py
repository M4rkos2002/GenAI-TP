from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="GenAI-TP",
    description="AI Agent for Slogan and Name Generation",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1") 