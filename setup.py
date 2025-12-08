from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="openimagen",
    version="1.0.0",
    author="OpenImagen Team",
    author_email="team@openimagen.dev",
    description="AI-Powered Professional Image Generation for Any Business Topic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/federicodeponte/openimagen",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0", 
            "flake8>=5.0.0",
            "mypy>=0.991",
        ],
        "examples": [
            "jupyter>=1.0.0",
            "matplotlib>=3.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "openimagen=openimagen.cli:main",
        ],
    },
    keywords="ai, image generation, business, professional, gemini, google ai, editorial, photography, content marketing",
    project_urls={
        "Bug Reports": "https://github.com/federicodeponte/openimagen/issues",
        "Source": "https://github.com/federicodeponte/openimagen",
        "Documentation": "https://github.com/federicodeponte/openimagen#readme",
    },
)