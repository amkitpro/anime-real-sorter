#!/usr/bin/env python3
"""
Dependency checker for Anime vs Real Image Sorter
Created by amkitpro
"""

import importlib.util
import subprocess
import sys

def check_package(package_name):
    """Check if a package is installed"""
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        return False, f"{package_name} is NOT installed"
    else:
        try:
            module = importlib.import_module(package_name)
            version = getattr(module, '__version__', 'unknown version')
            return True, f"{package_name} version {version}"
        except ImportError:
            return False, f"{package_name} is NOT installed properly"

def get_installed_version(package_name):
    """Get the installed version of a package"""
    try:
        if package_name == 'PIL':
            package_name = 'Pillow'
            
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'show', package_name
        ], capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    return line.split(': ')[1].strip()
        return "unknown (package found but version could not be determined)"
    except:
        return "unknown"

def main():
    """Main function to check all requirements"""
    print("=" * 60)
    print("Dependency Check for Anime vs Real Image Sorter")
    print("Created by amkitpro")
    print("=" * 60)
    
    # List of required packages
    required_packages = [
        'tensorflow',
        'PIL',  # This is Pillow
        'numpy',
        'tqdm',
        'deepdanbooru'
    ]
    
    all_installed = True
    for package in required_packages:
        installed, message = check_package(package)
        status = "✓" if installed else "✗"
        print(f"{status} {message}")
        if not installed:
            all_installed = False
    
    print("=" * 60)
    if all_installed:
        print("All dependencies are installed! You're ready to use the application.")
    else:
        print("Some dependencies are missing. Please install them with:")
        print("pip install tensorflow pillow numpy tqdm")
        print("pip install git+https://github.com/KichangKim/DeepDanbooru.git")
    
    print("=" * 60)

if __name__ == "__main__":
    main()