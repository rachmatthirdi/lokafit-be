"""
AI System #3: MixMatch Logic
Recommendation engine using color theory
"""
from typing import Dict, List, Tuple

class MixMatchRecommender:
    """Recommendation engine based on color theory"""
    
    def __init__(self):
        self.color_wheel = self._build_color_wheel()
    
    def get_instant_match(self, item_color_hex: str, user_undertone: str) -> Dict:
        """
        Get instant match recommendations based on color theory
        
        Args:
            item_color_hex: Hex color of current item (e.g., "#FF0000")
            user_undertone: User's undertone (Warm/Cool/Neutral)
            
        Returns:
            Dictionary with recommended item colors and match scores
        """
        try:
            # Convert hex to HSV for color theory
            h, s, v = self._hex_to_hsv(item_color_hex)
            
            # Get complementary colors
            complementary = self._get_complementary(h)
            
            # Get analogous colors
            analogous = self._get_analogous(h)
            
            # Get triadic colors
            triadic = self._get_triadic(h)
            
            # Filter by user undertone
            all_recommendations = []
            
            for color, score, theory in [
                (complementary, 0.95, "complementary"),
                (analogous[0], 0.85, "analogous"),
                (analogous[1], 0.85, "analogous"),
                (triadic[0], 0.90, "triadic"),
                (triadic[1], 0.90, "triadic"),
            ]:
                match_score = self._apply_undertone_filter(score, user_undertone)
                all_recommendations.append({
                    "color_hex": color,
                    "match_score": match_score,
                    "theory": theory
                })
            
            # Sort by match score
            all_recommendations.sort(key=lambda x: x["match_score"], reverse=True)
            
            return {
                "status": "success",
                "item_color": item_color_hex,
                "recommendations": all_recommendations[:5],  # Top 5
                "confidence": 0.88
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "confidence": 0.0
            }
    
    def _hex_to_hsv(self, hex_color: str) -> Tuple[float, float, float]:
        """Convert hex color to HSV"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        diff = max_c - min_c
        
        # Hue
        if max_c == r:
            h = (60 * ((g - b) / diff % 6)) if diff != 0 else 0
        elif max_c == g:
            h = (60 * ((b - r) / diff + 2)) if diff != 0 else 0
        else:
            h = (60 * ((r - g) / diff + 4)) if diff != 0 else 0
        
        # Saturation
        s = (diff / max_c) if max_c != 0 else 0
        
        # Value
        v = max_c
        
        return h % 360, s, v
    
    def _hsv_to_hex(self, h: float, s: float, v: float) -> str:
        """Convert HSV to hex color"""
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        
        r, g, b = int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)
        
        return f"#{r:02x}{g:02x}{b:02x}".upper()
    
    def _get_complementary(self, hue: float) -> str:
        """Get complementary color (opposite on color wheel)"""
        comp_hue = (hue + 180) % 360
        return self._hsv_to_hex(comp_hue, 0.8, 0.9)
    
    def _get_analogous(self, hue: float) -> Tuple[str, str]:
        """Get two analogous colors (adjacent on color wheel)"""
        analog1_hue = (hue + 30) % 360
        analog2_hue = (hue - 30) % 360
        
        return (
            self._hsv_to_hex(analog1_hue, 0.8, 0.9),
            self._hsv_to_hex(analog2_hue, 0.8, 0.9)
        )
    
    def _get_triadic(self, hue: float) -> Tuple[str, str]:
        """Get two triadic colors (120° apart)"""
        tri1_hue = (hue + 120) % 360
        tri2_hue = (hue + 240) % 360
        
        return (
            self._hsv_to_hex(tri1_hue, 0.8, 0.9),
            self._hsv_to_hex(tri2_hue, 0.8, 0.9)
        )
    
    def _apply_undertone_filter(self, score: float, undertone: str) -> float:
        """Apply undertone filter to match score"""
        undertone_boost = {
            "Warm": 1.0,
            "Cool": 0.95,
            "Neutral": 0.90
        }
        
        return score * undertone_boost.get(undertone, 1.0)
    
    def _build_color_wheel(self) -> Dict:
        """Build color wheel for reference"""
        return {
            "Red": 0,
            "Orange": 30,
            "Yellow": 60,
            "Green": 120,
            "Cyan": 180,
            "Blue": 240,
            "Purple": 270,
            "Magenta": 300,
        }

# Singleton instance
mixmatch_recommender = MixMatchRecommender()
