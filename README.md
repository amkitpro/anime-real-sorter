markdown
# Anime vs Real Image Sorter

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub release](https://img.shields.io/github/v/release/amkitpro/anime-real-sorter)
![GitHub downloads](https://img.shields.io/github/downloads/amkitpro/anime-real-sorter/total)

A Python application that automatically sorts images into "Anime" and "Real" categories using DeepDanbooru for image tagging and classification.

Created by **amkitpro**

## Features

- 🖼️ GUI interface for easy image sorting
- 🔍 Automatic classification using DeepDanbooru tags
- 📁 Batch processing of multiple images
- 👀 Real-time image preview and tag display
- 🧪 Dry-run mode for testing
- 📊 Progress tracking and logging
- 🖥️ Cross-platform support (Windows, macOS, Linux)

## Quick Start

### Windows:
1. Download the latest release from [Releases](https://github.com/amkitpro/anime-real-sorter/releases)
2. Extract the zip file
3. Double-click `run.bat`
4. Or run: `python anime_real_sorter.py`

### macOS/Linux:
```bash
# Download and extract the release
chmod +x run.sh
./run.sh
# Or run directly:
python anime_real_sorter.py
Installation
Method 1: Using Pre-packaged Release (Recommended)
Go to Releases

Download the latest version for your OS

Extract and run

Method 2: From Source
bash
# Clone the repository
git clone https://github.com/amkitpro/anime-real-sorter.git
cd anime-real-sorter

# Run the setup script
# Windows:
run.bat

# macOS/Linux:
./run.sh
Method 3: Manual Installation
bash
# Create virtual environment
python -m venv dd-env

# Activate environment
# Windows:
dd-env\Scripts\activate
# macOS/Linux:
source dd-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python anime_real_sorter.py
Usage
Download DeepDanbooru Project Files:

Visit DeepDanbooru Releases

Download the latest model (e.g., deepdanbooru-v3-20211112-sgd-e30.zip)

Extract to a folder (e.g., deepdanbooru_project)

Run the Application:

Select your source folder containing images to sort

Select the DeepDanbooru project folder

(Optional) Enable dry-run mode to test without moving files

Click "Start Sorting" to begin processing

Check Results:

Anime images → source_folder/anime/

Real images → source_folder/real/

File Structure
text
anime-real-sorter/
├── anime_real_sorter.py    # Main application
├── check_dependencies.py   # Dependency verification
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows launcher
├── run.sh                  # macOS/Linux launcher
├── .gitignore             # Git ignore rules
└── README.md              # This file
Dependencies
Python 3.7+

TensorFlow 2.0+

Pillow (PIL)

NumPy

tqdm

DeepDanbooru

Verify all dependencies are installed with:

bash
python check_dependencies.py
Troubleshooting
Common Issues
TensorFlow not found:

bash
pip install tensorflow
DeepDanbooru project not found:

Download from DeepDanbooru Releases

Extract to a folder and select it in the application

Memory errors:

Process smaller batches of images

Use a machine with more RAM

Application won't start:

bash
# Check dependencies
python check_dependencies.py

# Reinstall requirements
pip install -r requirements.txt
Getting Help
If you encounter issues:

Check the GitHub Issues page

Ensure all dependencies are installed correctly

Verify your DeepDanbooru project folder contains required files

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
DeepDanbooru by KichangKim for image tagging

TensorFlow team for the machine learning framework

Python community for excellent libraries and tools

Created by amkitpro - 2025