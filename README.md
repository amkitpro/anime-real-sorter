# Anime vs Real Image Sorter

A Python application that automatically sorts images into "Anime" and "Real" categories using DeepDanbooru for image tagging and classification.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Created by **amkitpro**

## Features

- 🖼️ GUI interface for easy image sorting
- 🔍 Automatic classification using DeepDanbooru tags
- 📁 Batch processing of multiple images
- 👀 Real-time image preview and tag display
- 🧪 Dry-run mode for testing
- 📊 Progress tracking and logging

## How It Works

The application uses DeepDanbooru to analyze images and extract tags. Images are classified as:
- **REAL**: If they contain tags like 'realistic', 'photorealistic', or 'real_life'
- **ANIME**: All other images

## Installation

1. Clone this repository:
```bash
git clone https://github.com/amkitpro/anime-real-sorter.git
cd anime-real-sorter