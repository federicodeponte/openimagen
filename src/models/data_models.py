"""
Data models for OpenImagen - Professional AI Image Generation
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CompanyData:
    """Company context for image generation."""
    name: str
    industry: str
    language: str = "en"
    custom_prompt_instructions: Optional[str] = None


@dataclass
class ImageRequest:
    """Request for image generation."""
    headline: str
    keyword: str
    company_data: CompanyData


@dataclass
class ImageResponse:
    """Response from image generation."""
    success: bool
    image_url: str = ""
    image_data: Optional[bytes] = None
    alt_text: str = ""
    generation_time_seconds: float = 0.0
    error: Optional[str] = None
    prompt_used: Optional[str] = None
    scene_description: Optional[str] = None