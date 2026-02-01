from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="AWS Production App")

APP_NAME = os.getenv("APP_NAME", "aws-production-app")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
VERSION = os.getenv("VERSION", "dev")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": APP_NAME,
        "environment": ENVIRONMENT,
        "time": datetime.utcnow().isoformat()
    }

@app.get("/info")
def info():
    return {
        "service": APP_NAME,
        "environment": ENVIRONMENT,
        "version": VERSION
    }

@app.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "example-item-1"},
            {"id": 2, "name": "example-item-2"}
        ]
    }
