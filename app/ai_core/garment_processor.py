"""
AI System #1: Garment Processor
Analyzes clothing images for color, type, and measurements
"""
import cv2
import numpy as np
from PIL import Image
import io
from typing import Dict, List, Tuple, Optional
import json

class GarmentProcessor:
    """Process garment images to extract color, type, and measurements"""
    
    def __init__(self):
        self.color_names = self._get_color_names()
    
    def process_garment(self, image_bytes: bytes) -> Dict:
        """
        Process a garment image and extract features
        
        Args:
            image_bytes: Raw image data
            
        Returns:
            Dictionary with extracted garment data
        """
        try:
            # Convert bytes to numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if image is None:
                raise ValueError("Invalid image format")
            
            # Extract dominant color
            color_hex, color_name = self._extract_dominant_color(image)
            
            # Extract measurements
            measurements = self._extract_measurements(image)
            
            # Detect garment type (basic classification)
            garment_type = self._classify_garment_type(image)
            
            return {
                "status": "success",
                "color_hex": color_hex,
                "color_name": color_name,
                "measurements": measurements,
                "garment_type": garment_type,
                "confidence": 0.85
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "confidence": 0.0
            }
    
    def _extract_dominant_color(self, image: np.ndarray) -> Tuple[str, str]:
        """
        Extract dominant color from image using KMeans clustering
        
        Returns:
            Tuple of (hex_color, color_name)
        """
        # Resize for faster processing
        image_resized = cv2.resize(image, (150, 150))
        
        # Reshape image to list of pixels
        pixels = image_resized.reshape((-1, 3))
        pixels = np.float32(pixels)
        
        # KMeans clustering to find dominant color
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        _, labels, centers = cv2.kmeans(pixels, 1, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        
        # Get the dominant color (center)
        dominant_color = centers[0].astype(int)
        
        # Convert BGR to RGB
        r, g, b = dominant_color[2], dominant_color[1], dominant_color[0]
        
        # Convert to HEX
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
        
        # Get color name
        color_name = self._get_color_name(r, g, b)
        
        return hex_color, color_name
    
    def _extract_measurements(self, image: np.ndarray) -> Dict:
        """Extract garment measurements from image"""
        height, width, _ = image.shape
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply threshold
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        
        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Find largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            return {
                "width_px": int(w),
                "height_px": int(h),
                "area_px": int(cv2.contourArea(largest_contour)),
                "image_width": width,
                "image_height": height
            }
        
        return {
            "width_px": width,
            "height_px": height,
            "area_px": width * height,
            "image_width": width,
            "image_height": height
        }
    
    def _classify_garment_type(self, image: np.ndarray) -> str:
        """Basic garment type classification"""
        height, width, _ = image.shape
        aspect_ratio = width / height if height > 0 else 0
        
        # Simple heuristic classification
        if aspect_ratio > 1.2:
            return "wide"  # Could be a jacket or outer
        elif aspect_ratio < 0.8:
            return "long"  # Could be pants or skirt
        else:
            return "standard"  # Could be a shirt or blouse
    
    def _get_color_name(self, r: int, g: int, b: int) -> str:
        """Convert RGB to color name"""
        colors = {
            "Red": {"r_range": (100, 255), "g_range": (0, 100), "b_range": (0, 100)},
            "Blue": {"r_range": (0, 100), "g_range": (0, 150), "b_range": (100, 255)},
            "Green": {"r_range": (0, 100), "g_range": (100, 255), "b_range": (0, 100)},
            "Yellow": {"r_range": (100, 255), "g_range": (100, 255), "b_range": (0, 100)},
            "Black": {"r_range": (0, 50), "g_range": (0, 50), "b_range": (0, 50)},
            "White": {"r_range": (150, 255), "g_range": (150, 255), "b_range": (150, 255)},
            "Gray": {"r_range": (50, 150), "g_range": (50, 150), "b_range": (50, 150)},
        }
        
        for color_name, ranges in colors.items():
            if (ranges["r_range"][0] <= r <= ranges["r_range"][1] and
                ranges["g_range"][0] <= g <= ranges["g_range"][1] and
                ranges["b_range"][0] <= b <= ranges["b_range"][1]):
                return color_name
        
        return "Unknown"
    
    def _get_color_names(self) -> Dict:
        """Get color palette"""
        return {
            "Red": "#FF0000",
            "Blue": "#0000FF",
            "Green": "#00FF00",
            "Yellow": "#FFFF00",
            "Black": "#000000",
            "White": "#FFFFFF",
            "Gray": "#808080",
        }

# Singleton instance
garment_processor = GarmentProcessor()
