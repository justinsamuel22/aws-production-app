from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="AWS Production App")

@app.get("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.utcnow().isoformat()
    }

@app.get("/info")
def info():
    return {
        "service": "aws-production-app",
        "environment": os.getenv("ENVIRONMENT", "local")
    }
