"""Health check endpoints"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "LokaFit Backend is running",
        "version": "1.0.0"
    }

@router.get("/health/detailed")
async def health_check_detailed():
    """Detailed health check"""
    return {
        "status": "healthy",
        "services": {
            "api": "running",
            "ai_garment": "ready",
            "ai_profile": "ready",
            "ai_recommend": "ready"
        }
    }
