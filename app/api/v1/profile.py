"""Profile analysis endpoints (AI System #2)"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.ai_core.profile_analyzer import profile_analyzer
from app.config import settings

router = APIRouter()

@router.post("/profile/skin-tone")
async def analyze_skin_tone(file: UploadFile = File(...)):
    """
    Analyze user's skin tone from face photo
    
    AI System #2: Profile Analyzer
    - Classifies skin tone (Light, Medium, Deep)
    - Determines undertone (Warm, Cool, Neutral)
    - Returns recommended color palette
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
    
    # Analyze skin tone
    result = profile_analyzer.analyze_skin_tone(contents)
    
    if result["status"] != "success":
        raise HTTPException(
            status_code=400,
            detail=result.get("message", "Failed to analyze skin tone")
        )
    
    return {
        "user_id": f"user_{file.filename.split('.')[0]}",
        "skin_tone": result["skin_tone"],
        "undertone": result["undertone"],
        "recommended_colors": result["recommended_colors"],
        "confidence": result["confidence"]
    }

@router.post("/profile/analyze")
async def analyze_full_profile(file: UploadFile = File(...)):
    """Full profile analysis (skin tone + color palette)"""
    
    contents = await file.read()
    result = profile_analyzer.analyze_skin_tone(contents)
    
    if result["status"] != "success":
        raise HTTPException(status_code=400, detail=result.get("message"))
    
    return result
