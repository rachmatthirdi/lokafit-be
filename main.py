from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from app.api.v1 import scan, profile, recommend, health

# Initialize FastAPI app
app = FastAPI(
    title="LokaFit Backend - AI Engine",
    description="Fashion styling assistant backend with AI-powered features",
    version="1.0.0"
)

# Configure CORS - Allow frontend to communicate
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://localhost:3000",
    "https://localhost:3001",
    "https://*.vercel.app",
    "https://lokafit.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(scan.router, prefix="/api/v1", tags=["scan"])
app.include_router(profile.router, prefix="/api/v1", tags=["profile"])
app.include_router(recommend.router, prefix="/api/v1", tags=["recommend"])

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "LokaFit Backend API - AI Engine",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
