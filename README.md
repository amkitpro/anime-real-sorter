# 🎨 Anime vs Real Image Sorter

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![GitHub release](https://img.shields.io/github/v/release/amkitpro/anime-vs-real-sorter)
![GitHub stars](https://img.shields.io/github/stars/amkitpro/anime-vs-real-sorter)
![GitHub forks](https://img.shields.io/github/forks/amkitpro/anime-vs-real-sorter)

A Python application that automatically sorts images into **Anime** and **Real** categories using **DeepDanbooru** for image tagging and classification.

---

## 📝 Features
- GUI interface for easy image sorting  
- Automatic classification using DeepDanbooru tags  
- Batch processing of multiple images  
- Real-time image preview and tag display  
- Dry-run mode for testing  
- Progress tracking and logging  
- Cross-platform support (Windows, macOS, Linux)  

---

## 🚀 Quick Start

### Windows
1. Download the latest release from [Releases](#)  
2. Extract the zip file  
3. Double-click `run.bat`  
4. Or run directly:  
```bash
python anime_real_sorter.py
```

### macOS / Linux
1. Download and extract the release  
2. Make launcher executable:  
```bash
chmod +x run.sh
```
3. Run the launcher:  
```bash
./run.sh
```
4. Or run directly:  
```bash
python anime_real_sorter.py
```

---

## ⚙️ Installation Methods

### 1. Using Pre-packaged Release (Recommended)
- Go to [Releases](#)  
- Download the latest version for your OS  
- Extract and run  

### 2. From Source
- Clone the repository  
```bash
git clone https://github.com/amkitpro/anime-vs-real-sorter.git
```
- Run the setup script: `run.bat` (Windows) or `run.sh` (macOS/Linux)  

### 3. Manual Installation
```bash
python -m venv dd-env
source dd-env/bin/activate  # On Windows: dd-env\Scripts\activate
pip install -r requirements.txt
python anime_real_sorter.py
```

---

## 🖼️ Usage
1. Download **DeepDanbooru Project Files** from [DeepDanbooru Releases](https://github.com/KichangKim/DeepDanbooru)  
2. Extract to a folder (e.g., `deepdanbooru_project`)  
3. Run the application and select **Source Folder** and **Project Folder**  
4. Click **Start Sorting**  

**Output Folders:**  
```
source_folder/anime/
source_folder/real/
```

---

## 📂 File Structure
- `anime_real_sorter.py` – Main application
- `check_dependencies.py` – Dependency verification
- `requirements.txt` – Python dependencies
- `run.bat` – Windows launcher
- `run.sh` – macOS/Linux launcher
- `.gitignore` – Git ignore rules
- `README.md` – Documentation

---

## 📦 Dependencies
- Python 3.7+
- TensorFlow 2.0+
- Pillow (PIL)
- NumPy
- tqdm
- DeepDanbooru

---

## 🛠️ Troubleshooting
- **TensorFlow not found:** `pip install tensorflow`
- **DeepDanbooru not found:** Download from DeepDanbooru Releases and extract to folder
- **Memory errors:** Process smaller batches or use machine with more RAM
- **Application won’t start:** Run `python check_dependencies.py` and `pip install -r requirements.txt`

---

## 🤝 Contributing
Contributions welcome! Fork repository, create a feature branch, commit changes, push to branch, and open a Pull Request.

---

## 📄 License
MIT License

---

## 🙏 Acknowledgments
- DeepDanbooru by KichangKim for image tagging
- TensorFlow team for machine learning framework
- Python community for excellent libraries and tools

---

## 🏷️ Badges
- Python version badge
- TensorFlow version badge
- MIT License badge
- GitHub release badge
- GitHub downloads badge
- GitHub stars badge
- GitHub forks badge

---

## 📌 Additional Sections
- Getting Help
- FAQ
- Changelog
- Roadmap
- Support