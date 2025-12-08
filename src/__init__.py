"""
OpenImagen - AI-Powered Professional Image Generation

A scalable, intelligent image generation system that creates editorial-quality
business images for ANY topic or industry using AI scene intelligence.

Key Features:
- AI-powered scene generation using Gemini 3.0 Pro
- Infinite scalability without hardcoded limitations  
- Editorial photography standards (Bloomberg/HBR quality)
- Gemini 3 Pro Image (Nano Banana Pro) generation
- Professional 16:9 format consistency
- Inclusive and diverse representation

Example Usage:

    from openimagen import generate_professional_image
    
    response = generate_professional_image(
        headline="Quantum Computing Revolution",
        keyword="quantum computing algorithms",
        company_name="QuantumTech",
        industry="Advanced Computing"
    )
    
    if response.success:
        with open("quantum_image.jpg", "wb") as f:
            f.write(response.image_data)
"""

from core.imagen_generator import OpenImagen, generate_professional_image
from models.data_models import ImageRequest, ImageResponse, CompanyData

__version__ = "1.0.0"
__author__ = "OpenImagen Team"

__all__ = [
    "OpenImagen", 
    "generate_professional_image",
    "ImageRequest",
    "ImageResponse", 
    "CompanyData"
]