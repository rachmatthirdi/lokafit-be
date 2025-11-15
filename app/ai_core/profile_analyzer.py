"""
AI System #2: Profile Analyzer
Analyzes skin tone and user preferences from photos
"""
import cv2
import numpy as np
from typing import Dict, Tuple

class ProfileAnalyzer:
    """Analyze user profile from photos"""
    
    def analyze_skin_tone(self, image_bytes: bytes) -> Dict:
        """
        Analyze skin tone from face photo
        
        Args:
            image_bytes: Raw image data
            
        Returns:
            Dictionary with skin tone analysis
        """
        try:
            # Convert bytes to numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if image is None:
                raise ValueError("Invalid image format")
            
            # Analyze skin tone
            skin_tone, undertone = self._classify_skin_tone(image)
            
            # Get recommended colors
            recommended_colors = self._get_recommended_colors(undertone)
            
            return {
                "status": "success",
                "skin_tone": skin_tone,
                "undertone": undertone,
                "recommended_colors": recommended_colors,
                "confidence": 0.80
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "confidence": 0.0
            }
    
    def _classify_skin_tone(self, image: np.ndarray) -> Tuple[str, str]:
        """
        Classify skin tone (Light, Medium, Deep)
        and undertone (Warm, Cool, Neutral)
        
        Returns:
            Tuple of (skin_tone, undertone)
        """
        # Get image center (usually face area)
        height, width, _ = image.shape
        center_y, center_x = height // 2, width // 2
        
        # Extract center region (approximate face area)
        h_margin = height // 4
        w_margin = width // 4
        face_region = image[
            max(0, center_y - h_margin):min(height, center_y + h_margin),
            max(0, center_x - w_margin):min(width, center_x + w_margin)
        ]
        
        # Calculate average color
        avg_color = cv2.mean(face_region)[:3]
        
        # Convert BGR to RGB
        r, g, b = avg_color[2], avg_color[1], avg_color[0]
        
        # Determine undertone based on RGB values
        if r > b:
            undertone = "Warm"
        elif b > r:
            undertone = "Cool"
        else:
            undertone = "Neutral"
        
        # Determine skin tone brightness
        brightness = (r + g + b) / 3
        
        if brightness > 180:
            skin_tone = "Light"
        elif brightness > 120:
            skin_tone = "Medium"
        else:
            skin_tone = "Deep"
        
        return skin_tone, undertone
    
    def _get_recommended_colors(self, undertone: str) -> list:
        """Get recommended color palette based on undertone"""
        palettes = {
            "Warm": [
                {"name": "Coral", "hex": "#FF6B6B"},
                {"name": "Peach", "hex": "#FFAB91"},
                {"name": "Gold", "hex": "#FFD700"},
                {"name": "Rust", "hex": "#B7410E"},
                {"name": "Earth Brown", "hex": "#8B6F47"},
            ],
            "Cool": [
                {"name": "Rose", "hex": "#FF69B4"},
                {"name": "Lavender", "hex": "#E6E6FA"},
                {"name": "Jewel Blue", "hex": "#0047AB"},
                {"name": "Berry", "hex": "#661D5C"},
                {"name": "Silver", "hex": "#C0C0C0"},
            ],
            "Neutral": [
                {"name": "Navy", "hex": "#000080"},
                {"name": "Burgundy", "hex": "#800020"},
                {"name": "Olive", "hex": "#808000"},
                {"name": "Taupe", "hex": "#B38B6D"},
                {"name": "Black", "hex": "#000000"},
            ]
        }
        
        return palettes.get(undertone, palettes["Neutral"])

# Singleton instance
profile_analyzer = ProfileAnalyzer()
