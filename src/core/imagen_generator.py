"""
OpenImagen - AI-Powered Professional Image Generation

Global intelligent image generation system that uses AI to create contextually 
appropriate professional images for ANY topic/industry combination.

Key Features:
- AI-powered scene generation using Gemini 3.0 Pro
- Infinite scalability without hardcoded industry limitations
- Editorial-quality photography standards
- Gemini 3 Pro Image (Nano Banana Pro) generation
- Intelligent fallback systems
"""

import os
import time
import base64
import logging
from typing import Optional

from ..models.data_models import ImageRequest, ImageResponse, CompanyData

logger = logging.getLogger(__name__)


class OpenImagen:
    """
    Professional AI image generation system.
    
    Uses Gemini 3 Pro Image (Nano Banana Pro) with AI-powered scene intelligence
    to create editorial-quality images for any business topic.
    """
    
    # Latest Gemini models
    IMAGE_MODEL = "gemini-3-pro-image-preview"  # Nano Banana Pro
    TEXT_MODEL = "gemini-3-pro-preview"  # For scene generation
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenImagen generator.
        
        Args:
            api_key: Google API key. If not provided, will look for environment variables.
        """
        # Get API key
        self.api_key = api_key or self._get_api_key()
        if not self.api_key:
            raise ValueError("Google API key required. Set GOOGLE_API_KEY environment variable or pass api_key parameter.")
        
        # Initialize Google GenAI client
        try:
            from google import genai
            from google.genai import types
            self.client = genai.Client(
                api_key=self.api_key,
                http_options=types.HttpOptions(api_version='v1alpha')
            )
            self._genai = genai
            self._types = types
            logger.info(f"OpenImagen initialized (model: {self.IMAGE_MODEL})")
        except ImportError:
            raise ImportError("google-genai package required. Install with: pip install google-genai")
    
    def _get_api_key(self) -> Optional[str]:
        """Get API key from environment variables."""
        return (os.getenv("GOOGLE_API_KEY") or 
                os.getenv("GEMINI_API_KEY") or 
                os.getenv("GOOGLE_GEMINI_API_KEY"))
    
    def generate_image(self, request: ImageRequest) -> ImageResponse:
        """
        Generate a professional editorial image for any business topic.
        
        Args:
            request: Image generation request with headline, keyword, and company data
            
        Returns:
            ImageResponse with image data and metadata
        """
        start_time = time.time()
        
        try:
            logger.info(f"Starting image generation for: {request.headline}")
            
            # Generate AI-powered scene description
            scene_description = self._generate_intelligent_scene(
                request.keyword, 
                request.company_data.industry
            )
            
            # Build professional prompt
            prompt = self._build_professional_prompt(request, scene_description)
            logger.info(f"Generated prompt ({len(prompt)} chars)")
            
            # Generate image using Gemini 3 Pro Image
            image_data = self._generate_with_retry(prompt)
            
            if image_data:
                # Create response
                generation_time = time.time() - start_time
                return ImageResponse(
                    success=True,
                    image_data=image_data,
                    image_url=f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}",
                    alt_text=self._generate_alt_text(request),
                    generation_time_seconds=generation_time,
                    prompt_used=prompt,
                    scene_description=scene_description
                )
            else:
                return ImageResponse(
                    success=False,
                    error="Failed to generate image after retries",
                    generation_time_seconds=time.time() - start_time
                )
                
        except Exception as e:
            logger.error(f"Image generation failed: {e}")
            return ImageResponse(
                success=False,
                error=str(e),
                generation_time_seconds=time.time() - start_time
            )
    
    def _generate_intelligent_scene(self, keyword: str, industry: str) -> str:
        """
        AI-powered scene generation using Gemini to create contextually appropriate
        scene descriptions for ANY topic/industry combination.
        """
        try:
            # Create focused prompt for scene generation
            scene_prompt = f\"\"\"Generate a professional, realistic scene description for a business editorial photograph about "{keyword}" in the {industry} industry.

Requirements:
- Describe a specific, photographable workplace scene (not abstract concepts)
- Focus on real people doing authentic work related to this topic
- Include environmental details that make it feel genuine and lived-in
- Avoid generic office descriptions - be specific to the topic
- Maximum 2 sentences, around 30-40 words
- Professional but not sterile - show real work happening

Examples of good scene descriptions:
- "Software engineer explaining code architecture to colleagues at a standing desk, laptops open with multiple monitors showing data visualizations. Coffee cups and notebooks scattered naturally."
- "Construction supervisor reviewing safety protocols with team on-site, hard hats and high-vis vests visible. Building materials and equipment in background under natural daylight."
- "Healthcare administrator analyzing patient flow data on tablet in hospital corridor. Medical staff moving naturally in background, professional but warm atmosphere."

Generate scene description for: {keyword} ({industry} industry)\"\"\"
            
            # Use Gemini to generate scene
            response = self.client.models.generate_content(
                model=self.TEXT_MODEL,
                contents=scene_prompt,
                config=self._types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=100,
                    response_mime_type="text/plain"
                )
            )
            
            if response and response.text:
                scene_desc = response.text.strip().strip('"').strip("'")
                # Ensure reasonable length
                if len(scene_desc) > 200:
                    scene_desc = scene_desc[:200].rsplit('.', 1)[0] + '.'
                return scene_desc
                
        except Exception as e:
            logger.warning(f"AI scene generation failed, using intelligent fallback: {e}")
        
        # Intelligent fallback based on keyword analysis
        return self._create_intelligent_fallback(keyword, industry)
    
    def _create_intelligent_fallback(self, keyword: str, industry: str) -> str:
        """
        Intelligent fallback that analyzes keywords to create appropriate scenes
        without hardcoded mappings.
        """
        keyword_lower = keyword.lower()
        
        # Analyze keyword patterns intelligently
        if any(term in keyword_lower for term in ['ai', 'artificial intelligence', 'machine learning', 'automation', 'algorithm', 'data', 'software', 'tech', 'digital']):
            return f"Professional team collaborating on {keyword} in modern office environment. Multiple screens with data visualizations, authentic working session with natural lighting and lived-in details."
        
        elif any(term in keyword_lower for term in ['management', 'strategy', 'leadership', 'business', 'operations', 'planning', 'growth']):
            return f"Business professionals engaged in strategic discussion about {keyword}. Conference room setting with whiteboards, documents, and authentic decision-making atmosphere."
        
        elif any(term in keyword_lower for term in ['safety', 'security', 'compliance', 'risk', 'audit', 'quality']):
            return f"Professional reviewing {keyword} protocols in workplace setting. Documentation, monitoring equipment, and safety-focused environment with natural workflow."
        
        elif any(term in keyword_lower for term in ['customer', 'service', 'support', 'client', 'user', 'experience']):
            return f"Service professional engaged in {keyword} activities. Customer-facing environment with modern tools, authentic service delivery moment."
        
        elif any(term in keyword_lower for term in ['financial', 'finance', 'budget', 'cost', 'roi', 'investment', 'accounting']):
            return f"Finance professional analyzing {keyword} data at workstation. Multiple monitors with charts and reports, traditional yet modern office environment."
        
        # Generic professional scene that works for any topic
        return f"Professional team working on {keyword} project in contemporary workplace. Collaborative environment with modern tools, authentic work session with natural lighting and personal touches."
    
    def _build_professional_prompt(self, request: ImageRequest, scene_description: str) -> str:
        """
        Build professional editorial prompt with global standards.
        """
        prompt_parts = [
            # Global editorial standard
            f"Professional editorial photograph for a business article about '{request.keyword}'.",
            f"",
            f"Scene: {scene_description}",
            f"",
            # Universal photography standards
            f"Photography style:",
            f"- Professional editorial quality (Canon 5D Mark IV, 35mm f/2.8)",
            f"- Natural lighting with soft shadows, not harsh or uniform",
            f"- Rule of thirds composition, authentic documentary style",
            f"- Shallow depth of field with natural background blur",
            f"- Modern color grading with professional warmth",
            f"- Subtle film grain for authenticity",
            f"",
            # Universal editorial standards
            f"Editorial requirements:",
            f"- Candid, authentic moment - not posed or stock-photo-like",
            f"- Real workplace environment with natural details",
            f"- Professional but approachable atmosphere",
            f"- No text, logos, or branding visible in image",
            f"- Diverse and inclusive representation when people are shown",
            f"",
            # Technical specifications
            f"Technical specs: 16:9 landscape, high resolution, editorial quality",
            f"Style reference: Bloomberg Businessweek, Harvard Business Review",
        ]
        
        # Add custom requirements if specified
        if request.company_data.custom_prompt_instructions:
            prompt_parts.extend([
                f"",
                f"Additional requirements: {request.company_data.custom_prompt_instructions}",
            ])
        
        return "\\n".join(prompt_parts)
    
    def _generate_with_retry(self, prompt: str, max_retries: int = 3) -> Optional[bytes]:
        """
        Generate image with retry logic.
        """
        for attempt in range(max_retries):
            try:
                logger.debug(f"Image generation attempt {attempt + 1}/{max_retries}")
                
                response = self.client.models.generate_content(
                    model=self.IMAGE_MODEL,
                    contents=prompt,
                    config=self._types.GenerateContentConfig(
                        response_modalities=[self._types.Modality.TEXT, self._types.Modality.IMAGE]
                    )
                )
                
                # Extract image from response
                image_bytes = self._extract_image_from_response(response)
                if image_bytes:
                    logger.info(f"✅ Successfully generated image ({len(image_bytes)} bytes)")
                    return image_bytes
                
                logger.warning(f"No image in response, retrying ({attempt + 1}/{max_retries})")
                time.sleep(5 * (attempt + 1))  # Exponential backoff
                
            except Exception as e:
                logger.error(f"Generation attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5 * (attempt + 1))
                else:
                    raise
        
        return None
    
    def _extract_image_from_response(self, response) -> Optional[bytes]:
        """Extract image bytes from Gemini response."""
        try:
            if not response or not hasattr(response, 'candidates'):
                return None
            
            for candidate in response.candidates:
                if not hasattr(candidate, 'content') or not hasattr(candidate.content, 'parts'):
                    continue
                
                for part in candidate.content.parts:
                    if hasattr(part, 'inline_data'):
                        inline_data = part.inline_data
                        if hasattr(inline_data, 'data'):
                            image_data = inline_data.data
                            
                            if isinstance(image_data, bytes) and len(image_data) > 100:
                                # Check for valid image formats (JPEG or PNG)
                                if image_data[:3] == b'\\xff\\xd8\\xff' or image_data[:8] == b'\\x89PNG\\r\\n\\x1a\\n':
                                    return image_data
            
            return None
            
        except Exception as e:
            logger.error(f"Error extracting image: {e}")
            return None
    
    def _generate_alt_text(self, request: ImageRequest) -> str:
        """Generate accessibility-friendly alt text."""
        alt_text = f"Professional editorial image: {request.headline}"
        
        # Ensure reasonable length for accessibility
        if len(alt_text) > 125:
            alt_text = alt_text[:122] + "..."
        
        return alt_text


# Convenience function for quick usage
def generate_professional_image(
    headline: str,
    keyword: str, 
    company_name: str,
    industry: str,
    api_key: Optional[str] = None,
    custom_instructions: Optional[str] = None
) -> ImageResponse:
    """
    Quick function to generate a professional business image.
    
    Args:
        headline: Article headline
        keyword: Main keyword/topic
        company_name: Company name
        industry: Industry/sector
        api_key: Google API key (optional, will use environment variable)
        custom_instructions: Additional prompt instructions (optional)
    
    Returns:
        ImageResponse with generated image
    
    Example:
        response = generate_professional_image(
            headline="AI Revolution in Healthcare",
            keyword="artificial intelligence medical diagnosis",
            company_name="MedTech AI",
            industry="Healthcare Technology",
            custom_instructions="Focus on diverse medical professionals"
        )
        
        if response.success:
            with open("healthcare_ai.jpg", "wb") as f:
                f.write(response.image_data)
    """
    generator = OpenImagen(api_key=api_key)
    
    company_data = CompanyData(
        name=company_name,
        industry=industry,
        custom_prompt_instructions=custom_instructions
    )
    
    request = ImageRequest(
        headline=headline,
        keyword=keyword,
        company_data=company_data
    )
    
    return generator.generate_image(request)