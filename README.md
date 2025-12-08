# OpenImagen 🎨

**AI-Powered Professional Image Generation for Any Business Topic**

OpenImagen is a revolutionary image generation system that uses AI intelligence to create editorial-quality business images for ANY topic or industry combination. No more hardcoded limitations - infinite scalability powered by Gemini 3 Pro Image.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini 3 Pro](https://img.shields.io/badge/AI-Gemini%203%20Pro-brightgreen.svg)](https://ai.google.dev/gemini-api)

## ✨ Key Features

🧠 **AI-Powered Scene Intelligence** - Uses Gemini 3.0 Pro to generate contextually appropriate scenes for any business topic

🚀 **Infinite Scalability** - No hardcoded industry limitations. Works with aerospace, marine science, cryptocurrency, agriculture, or any field

📸 **Editorial Quality** - Bloomberg Businessweek and Harvard Business Review photography standards

🎯 **Professional Standards** - 16:9 format, Canon 5D Mark IV specifications, authentic documentary style

🌍 **Inclusive by Default** - Diverse and inclusive representation automatically considered

⚡ **Latest Technology** - Gemini 3 Pro Image (Nano Banana Pro) for state-of-the-art generation

## 🚀 Quick Start

### Installation

```bash
pip install google-genai
```

### Basic Usage

```python
from openimagen import generate_professional_image

# Generate image for any business topic
response = generate_professional_image(
    headline="Quantum Computing in Space Exploration", 
    keyword="quantum computing space missions algorithms",
    company_name="CosmicTech",
    industry="Aerospace Technology"
)

if response.success:
    # Save the professional image
    with open("space_quantum.jpg", "wb") as f:
        f.write(response.image_data)
    
    print(f"✅ Generated in {response.generation_time_seconds:.1f}s")
    print(f"Scene: {response.scene_description}")
else:
    print(f"❌ Error: {response.error}")
```

### Advanced Usage

```python
from openimagen import OpenImagen, ImageRequest, CompanyData

# Initialize generator
generator = OpenImagen(api_key="your-google-api-key")

# Create request with custom instructions
company_data = CompanyData(
    name="FemTech Leaders",
    industry="Technology", 
    custom_prompt_instructions="Focus on diverse female professionals in leadership roles"
)

request = ImageRequest(
    headline="Women Leading Tech Innovation",
    keyword="women tech leadership diversity",
    company_data=company_data
)

# Generate image
response = generator.generate_image(request)
```

## 🎯 Use Cases

### ✅ Perfect For:

- **Content Marketing** - Professional blog images for any industry
- **Social Media** - Editorial-quality posts that stand out  
- **Corporate Communications** - Authentic workplace imagery
- **Website Design** - Professional hero images and illustrations
- **Presentations** - High-quality business visuals
- **Marketing Materials** - Custom imagery for any business topic

### 🏆 Works With Any Industry:

- 🚀 **Aerospace** - Space exploration, satellite technology
- 🧬 **Biotech** - Gene therapy, pharmaceutical research  
- 🌱 **AgriTech** - Precision farming, vertical agriculture
- 💰 **FinTech** - Cryptocurrency, blockchain, digital banking
- 🏥 **HealthTech** - Medical devices, telemedicine
- 🏗️ **Construction** - Smart buildings, safety management
- 🌊 **Marine Science** - Ocean research, marine conservation
- **...and literally any other field!**

## 🎨 Image Quality Examples

### Technology Sector
![AI Customer Service](examples/ai_customer_service.jpg)
*AI-powered customer service automation*

### Healthcare Sector  
![Medical Innovation](examples/medical_devices.jpg)
*Medical device surgical innovation*

### Agriculture Sector
![Precision Farming](examples/precision_agriculture.jpg)
*Precision agriculture IoT sensors*

### Energy Sector
![Renewable Energy](examples/renewable_energy.jpg)
*Solar energy grid solutions*

## 🔧 Configuration

### Environment Variables

```bash
# Required: Google API key for Gemini
export GOOGLE_API_KEY="your-api-key-here"

# Alternative names also supported
export GEMINI_API_KEY="your-api-key-here" 
export GOOGLE_GEMINI_API_KEY="your-api-key-here"
```

### API Key Setup

1. Get a Google AI API key from [Google AI Studio](https://aistudio.google.com/)
2. Set the environment variable or pass directly to the generator
3. Start generating professional images!

## 📊 Performance

- **Generation Time**: 15-25 seconds average
- **Image Quality**: Editorial-grade (750-850KB JPEG)
- **Format**: Professional 16:9 landscape
- **Resolution**: High-resolution suitable for print and digital
- **Success Rate**: >95% with intelligent fallback systems

## 🏗️ Architecture

### AI-Powered Scene Generation

```
User Input → Gemini 3.0 Pro (Scene Analysis) → Professional Prompt → Gemini 3 Pro Image → Editorial Photo
```

1. **Intelligent Scene Analysis** - AI analyzes topic/industry to generate appropriate workplace scenes
2. **Professional Prompt Engineering** - Creates photography-grade prompts with technical specifications  
3. **Image Generation** - Uses latest Gemini 3 Pro Image (Nano Banana Pro) for superior quality
4. **Quality Assurance** - Validates output and provides detailed metadata

### Fallback Systems

- **AI Scene Generation** (Primary) - Contextual intelligence for any topic
- **Pattern Recognition** (Secondary) - Keyword analysis for scene selection
- **Generic Professional** (Tertiary) - Universal business scene guaranteed to work

## 🔍 API Reference

### `generate_professional_image()`

Quick function for simple use cases.

**Parameters:**
- `headline` (str): Article or content headline
- `keyword` (str): Main topic/keyword for the image
- `company_name` (str): Company name for context
- `industry` (str): Industry or business sector  
- `api_key` (str, optional): Google API key
- `custom_instructions` (str, optional): Additional prompt requirements

**Returns:** `ImageResponse` object

### `OpenImagen` Class

Full-featured generator for advanced use cases.

**Methods:**
- `__init__(api_key)`: Initialize generator
- `generate_image(request)`: Generate image from ImageRequest
- Professional prompt building and scene generation

### Data Models

**`ImageRequest`**
```python
@dataclass
class ImageRequest:
    headline: str
    keyword: str 
    company_data: CompanyData
```

**`ImageResponse`**
```python
@dataclass 
class ImageResponse:
    success: bool
    image_data: bytes
    image_url: str
    alt_text: str
    generation_time_seconds: float
    scene_description: str
    prompt_used: str
    error: Optional[str]
```

## 🚀 Why OpenImagen?

### vs. Traditional Stock Photos
- ❌ **Stock Photos**: Generic, overused, expensive licensing
- ✅ **OpenImagen**: Custom, contextual, one-time generation cost

### vs. Other AI Image Generators  
- ❌ **Others**: Generic prompts, inconsistent quality, limited business focus
- ✅ **OpenImagen**: Business-optimized, editorial standards, infinite scalability

### vs. Hardcoded Systems
- ❌ **Hardcoded**: Limited industries, maintenance overhead, breaks with new topics
- ✅ **OpenImagen**: AI-powered, handles any industry, zero maintenance

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/federicodeponte/openimagen.git
cd openimagen
pip install -r requirements.txt
pip install -e .
```

### Running Tests

```bash
python -m pytest tests/
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google AI** - For the incredible Gemini 3 Pro Image (Nano Banana Pro) model
- **OpenBlog Project** - Where this technology was first developed and tested
- **Business Photography Standards** - Inspired by Bloomberg Businessweek and Harvard Business Review

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/federicodeponte/openimagen/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/federicodeponte/openimagen/discussions)
- 📧 **Email**: support@openimagen.dev

---

**Made with ❤️ for the business content community**

*Professional images for every business story, powered by AI intelligence.*