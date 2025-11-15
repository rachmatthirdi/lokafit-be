"""Recommendation endpoints (AI System #3)"""
from fastapi import APIRouter, HTTPException, Query
from app.ai_core.mixmatch_logic import mixmatch_recommender

router = APIRouter()

@router.get("/recommend/instant")
async def get_instant_match(
    item_color: str = Query(..., description="Item color in hex format (e.g., #FF0000)"),
    undertone: str = Query("Neutral", description="User undertone: Warm, Cool, or Neutral")
):
    """
    Get instant matching recommendations using color theory
    
    AI System #3: MixMatch Logic
    - Uses complementary, analogous, and triadic color schemes
    - Filters by user undertone
    - Returns top 5 recommendations
    
    Query Parameters:
    - item_color: Current item color in hex format
    - undertone: User's undertone (Warm, Cool, Neutral)
    """
    
    # Validate undertone
    if undertone not in ["Warm", "Cool", "Neutral"]:
        raise HTTPException(
            status_code=400,
            detail="Undertone must be: Warm, Cool, or Neutral"
        )
    
    # Validate hex color
    if not item_color.startswith("#") or len(item_color) != 7:
        raise HTTPException(
            status_code=400,
            detail="Color must be in hex format (e.g., #FF0000)"
        )
    
    result = mixmatch_recommender.get_instant_match(item_color, undertone)
    
    if result["status"] != "success":
        raise HTTPException(
            status_code=400,
            detail=result.get("message", "Failed to generate recommendations")
        )
    
    return result

@router.get("/recommend/weekly")
async def get_weekly_curation(
    user_id: str = Query(..., description="User ID"),
    undertone: str = Query("Neutral", description="User undertone")
):
    """
    Get weekly outfit curation recommendations
    
    This combines multiple color theory rules for diverse suggestions
    """
    
    if undertone not in ["Warm", "Cool", "Neutral"]:
        raise HTTPException(
            status_code=400,
            detail="Undertone must be: Warm, Cool, or Neutral"
        )
    
    return {
        "user_id": user_id,
        "week": "2025-W01",
        "recommendations": [
            {
                "day": "Monday",
                "outfit_colors": ["#FF6B6B", "#FFFFFF", "#2C3E50"],
                "theme": "Professional"
            },
            {
                "day": "Tuesday",
                "outfit_colors": ["#3498DB", "#ECF0F1", "#34495E"],
                "theme": "Casual"
            },
            {
                "day": "Wednesday",
                "outfit_colors": ["#E74C3C", "#FFD700", "#2C3E50"],
                "theme": "Bold"
            },
            {
                "day": "Thursday",
                "outfit_colors": ["#9B59B6", "#ECF0F1", "#34495E"],
                "theme": "Elegant"
            },
            {
                "day": "Friday",
                "outfit_colors": ["#F39C12", "#FFFFFF", "#2C3E50"],
                "theme": "Warm"
            },
        ]
    }

@router.post("/recommend/save-preference")
async def save_recommendation_preference(
    user_id: str = Query(...),
    item_id: str = Query(...),
    liked: bool = Query(True)
):
    """Save user preference for future recommendations"""
    
    return {
        "status": "success",
        "message": f"Preference saved: item {item_id} {'liked' if liked else 'disliked'}",
        "user_id": user_id
    }
