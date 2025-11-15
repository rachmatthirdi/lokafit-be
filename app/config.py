import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application configuration"""
    
    # Environment
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = ENVIRONMENT == "development"
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    
    # API
    API_V1_STR = "/api/v1"
    API_TITLE = "LokaFit Backend"
    
    # AI Models
    AI_CONFIDENCE_THRESHOLD = float(os.getenv("AI_CONFIDENCE_THRESHOLD", "0.7"))
    
    # File upload
    MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
    
    # Color system
    COLOR_PALETTE_COUNT = 5  # Number of dominant colors to extract

settings = Settings()
