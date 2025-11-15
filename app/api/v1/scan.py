"""Garment scanning endpoints (AI System #1)"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ai_core.garment_processor import garment_processor
from app.config import settings
import io

router = APIRouter()

@router.post("/scan/accurate")
async def scan_garment_accurate(file: UploadFile = File(...)):
    """
    Scan garment image with accurate color extraction
    
    AI System #1: Garment Processor
    - Extracts dominant color using KMeans
    - Measures garment dimensions
    - Classifies garment type
    """
    
    # Validate file
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Accepted: JPEG, PNG, WebP"
        )
    
    # Read file
    contents = await file.read()
    
    if len(contents) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Max size: {settings.MAX_UPLOAD_SIZE} bytes"
        )
    
    # Process garment
    result = garment_processor.process_garment(contents)
    
    if result["status"] != "success":
        raise HTTPException(
            status_code=400,
            detail=result.get("message", "Failed to process garment")
        )
    
    return {
        "garment_id": f"garment_{file.filename.split('.')[0]}",
        "color_hex": result["color_hex"],
        "color_name": result["color_name"],
        "garment_type": result["garment_type"],
        "measurements": result["measurements"],
        "confidence": result["confidence"],
        "image_url": f"/images/{file.filename}"
    }

@router.post("/scan/quick")
async def scan_garment_quick(file: UploadFile = File(...)):
    """Quick color extraction without detailed measurements"""
    
    # Validate file
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type"
        )
    
    contents = await file.read()
    result = garment_processor.process_garment(contents)
    
    if result["status"] != "success":
        raise HTTPException(status_code=400, detail=result.get("message"))
    
    return {
        "color_hex": result["color_hex"],
        "color_name": result["color_name"],
        "confidence": result["confidence"]
    }
