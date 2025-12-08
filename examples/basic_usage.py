#!/usr/bin/env python3
"""
OpenImagen Basic Usage Examples

Demonstrates how to generate professional business images for any topic.
"""

import os
import sys
sys.path.insert(0, '../src')
from core.imagen_generator import generate_professional_image, OpenImagen
from models.data_models import ImageRequest, CompanyData


def example_1_quick_generation():
    """Quick image generation for any business topic."""
    print("🚀 Example 1: Quick Professional Image Generation")
    print("=" * 50)
    
    # Generate image for a novel industry combination
    response = generate_professional_image(
        headline="Quantum Computing in Marine Biology",
        keyword="quantum computing marine research data analysis", 
        company_name="OceanQuantum",
        industry="Marine Technology"
    )
    
    if response.success:
        # Save the image
        with open("quantum_marine_biology.jpg", "wb") as f:
            f.write(response.image_data)
        
        print(f"✅ Generated in {response.generation_time_seconds:.1f} seconds")
        print(f"📸 Image saved as: quantum_marine_biology.jpg")
        print(f"🎬 Scene: {response.scene_description}")
        print(f"📝 Alt text: {response.alt_text}")
        
    else:
        print(f"❌ Generation failed: {response.error}")


def example_2_custom_instructions():
    """Advanced usage with custom prompt instructions."""
    print("\n🎯 Example 2: Custom Instructions for Specific Requirements")
    print("=" * 60)
    
    # Use advanced generator with custom instructions
    generator = OpenImagen()
    
    company_data = CompanyData(
        name="DiverseTech",
        industry="Technology",
        custom_prompt_instructions="Focus on diverse professionals including women and minorities in leadership roles, modern sustainable office environment"
    )
    
    request = ImageRequest(
        headline="Inclusive Leadership in AI Development",
        keyword="diverse AI team leadership inclusive technology",
        company_data=company_data
    )
    
    response = generator.generate_image(request)
    
    if response.success:
        with open("inclusive_ai_leadership.jpg", "wb") as f:
            f.write(response.image_data)
            
        print(f"✅ Generated in {response.generation_time_seconds:.1f} seconds") 
        print(f"📸 Image saved as: inclusive_ai_leadership.jpg")
        print(f"🎬 AI Scene: {response.scene_description}")
        print(f"🎨 Custom requirements applied successfully")
        
    else:
        print(f"❌ Generation failed: {response.error}")


def example_3_unusual_industries():
    """Test scalability with completely novel industry combinations."""
    print("\n🧪 Example 3: Testing Scalability with Novel Industries")
    print("=" * 55)
    
    # Test cases that would break hardcoded systems
    test_cases = [
        {
            "headline": "Blockchain in Space Agriculture", 
            "keyword": "blockchain space farming satellite agriculture",
            "company": "CosmicFarm",
            "industry": "Space Agriculture"
        },
        {
            "headline": "AI-Powered Jewelry Design",
            "keyword": "artificial intelligence jewelry design customization", 
            "company": "SmartJewels",
            "industry": "Fashion Technology"
        },
        {
            "headline": "Cryptocurrency Mining with Renewable Energy",
            "keyword": "cryptocurrency mining solar wind renewable energy",
            "company": "GreenCoin",
            "industry": "Sustainable Cryptocurrency"
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        print(f"\n🔬 Test {i}: {case['industry']} - {case['headline']}")
        print("-" * 40)
        
        response = generate_professional_image(
            headline=case["headline"],
            keyword=case["keyword"], 
            company_name=case["company"],
            industry=case["industry"]
        )
        
        if response.success:
            filename = f"novel_industry_{i}.jpg"
            with open(filename, "wb") as f:
                f.write(response.image_data)
            print(f"✅ SUCCESS! Generated {filename} in {response.generation_time_seconds:.1f}s")
            print(f"Scene: {response.scene_description[:80]}...")
        else:
            print(f"❌ Failed: {response.error}")


def example_4_batch_generation():
    """Generate multiple images for a content series."""
    print("\n📚 Example 4: Batch Generation for Content Series")
    print("=" * 50)
    
    # Content series about emerging technologies
    series_topics = [
        ("Edge Computing Revolution", "edge computing IoT distributed systems", "EdgeTech Solutions", "Computing Infrastructure"),
        ("Vertical Farming Innovation", "vertical farming hydroponics smart agriculture", "UrbanGrow", "Agricultural Technology"), 
        ("Quantum Cryptography Security", "quantum cryptography cybersecurity encryption", "QuantumSecure", "Cybersecurity Technology")
    ]
    
    print(f"Generating {len(series_topics)} professional images for content series...")
    
    for i, (headline, keyword, company, industry) in enumerate(series_topics, 1):
        print(f"\n📸 Generating image {i}/{len(series_topics)}: {headline}")
        
        response = generate_professional_image(
            headline=headline,
            keyword=keyword,
            company_name=company, 
            industry=industry
        )
        
        if response.success:
            filename = f"series_image_{i}_{keyword.split()[0]}.jpg"
            with open(filename, "wb") as f:
                f.write(response.image_data)
            print(f"   ✅ Saved {filename} ({response.generation_time_seconds:.1f}s)")
        else:
            print(f"   ❌ Failed: {response.error}")
    
    print(f"\n🎉 Content series generation complete!")


def main():
    """Run all examples."""
    print("OpenImagen - Professional AI Image Generation Examples")
    print("=" * 60)
    
    # Check for API key
    if not any(os.getenv(key) for key in ["GOOGLE_API_KEY", "GEMINI_API_KEY", "GOOGLE_GEMINI_API_KEY"]):
        print("❌ No API key found!")
        print("Please set GOOGLE_API_KEY environment variable:")
        print("export GOOGLE_API_KEY='your-api-key-here'")
        return
    
    try:
        # Run examples
        example_1_quick_generation()
        example_2_custom_instructions()
        example_3_unusual_industries() 
        example_4_batch_generation()
        
        print("\n🎉 All examples completed successfully!")
        print("Check the generated .jpg files to see the professional quality.")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure you have a valid Google API key and internet connection.")


if __name__ == "__main__":
    main()