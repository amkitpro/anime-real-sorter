import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import subprocess
import sys
from PIL import Image, ImageTk
import shutil
import importlib.util

class DeepDanbooruSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Anime vs Real Image Sorter")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Variables
        self.source_folder = tk.StringVar()
        self.project_path = tk.StringVar()
        self.dry_run = tk.BooleanVar(value=False)
        self.processing = False
        self.current_image_tags = {}
        self.python_executable = sys.executable
        
        # Check if TensorFlow is available
        self.tensorflow_available = importlib.util.find_spec("tensorflow") is not None
        
        # Setup UI
        self.setup_ui()
        
        if not self.tensorflow_available:
            self.log_message("WARNING: TensorFlow not found. Please install it with: pip install tensorflow")
        else:
            self.log_message("All dependencies are available. Ready to process images.")
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Anime vs Real Image Sorter", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Python executable info
        ttk.Label(main_frame, text="Python Executable:").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(main_frame, text=self.python_executable).grid(row=1, column=1, sticky=tk.W, pady=2)
        
        # TensorFlow status
        status_text = "Available" if self.tensorflow_available else "NOT FOUND - Please install TensorFlow"
        status_color = "green" if self.tensorflow_available else "red"
        ttk.Label(main_frame, text="TensorFlow Status:").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Label(main_frame, text=status_text, foreground=status_color).grid(row=2, column=1, sticky=tk.W, pady=2)
        
        # Source folder selection
        ttk.Label(main_frame, text="Source Folder:").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.source_folder, width=50).grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_source).grid(row=3, column=2, padx=5, pady=5)
        
        # Project path selection
        ttk.Label(main_frame, text="DeepDanbooru Project:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.project_path, width=50).grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_project).grid(row=4, column=2, padx=5, pady=5)
        
        # Options
        ttk.Checkbutton(main_frame, text="Dry Run (don't move files)", variable=self.dry_run).grid(row=5, column=1, sticky=tk.W, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=10)
        ttk.Button(button_frame, text="Start Sorting", command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Stop", command=self.stop_sorting).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Test Single Image", command=self.test_single_image).pack(side=tk.LEFT, padx=5)
        
        # Progress
        ttk.Label(main_frame, text="Progress:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=7, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Ready")
        self.status_label.grid(row=8, column=0, columnspan=3, sticky=tk.W, pady=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="5")
        results_frame.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Create notebook for different views
        notebook = ttk.Notebook(results_frame)
        notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Image preview tab
        preview_frame = ttk.Frame(notebook, padding="5")
        notebook.add(preview_frame, text="Image Preview")
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(1, weight=1)
        
        ttk.Label(preview_frame, text="Current Image:").grid(row=0, column=0, sticky=tk.W)
        self.image_label = ttk.Label(preview_frame, text="No image selected")
        self.image_label.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Tags tab
        tags_frame = ttk.Frame(notebook, padding="5")
        notebook.add(tags_frame, text="Tags")
        tags_frame.columnconfigure(0, weight=1)
        tags_frame.rowconfigure(0, weight=1)
        
        # Tags text area
        self.tags_text = tk.Text(tags_frame, height=10, wrap=tk.WORD)
        tags_scrollbar = ttk.Scrollbar(tags_frame, orient=tk.VERTICAL, command=self.tags_text.yview)
        self.tags_text.configure(yscrollcommand=tags_scrollbar.set)
        
        self.tags_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tags_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Log tab
        log_frame = ttk.Frame(notebook, padding="5")
        notebook.add(log_frame, text="Log")
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        # Log text area
        self.log_text = tk.Text(log_frame, height=10, wrap=tk.WORD)
        log_scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Footer
        footer_label = ttk.Label(main_frame, text="Created by amkitpro", foreground="gray")
        footer_label.grid(row=10, column=0, columnspan=3, pady=10)
        
        # Configure weights for expansion
        main_frame.rowconfigure(9, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def browse_source(self):
        folder = filedialog.askdirectory(title="Select Source Folder")
        if folder:
            self.source_folder.set(folder)
            
    def browse_project(self):
        folder = filedialog.askdirectory(title="Select DeepDanbooru Project Folder")
        if folder:
            self.project_path.set(folder)
            
    def log_message(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.status_label.config(text=message)
        
    def start_sorting(self):
        if not self.source_folder.get():
            messagebox.showerror("Error", "Please select a source folder")
            return
            
        if not self.project_path.get():
            messagebox.showerror("Error", "Please select a DeepDanbooru project folder")
            return
            
        self.processing = True
        self.progress.start()
        self.log_message("Starting sorting process...")
        
        thread = threading.Thread(target=self.process_images)
        thread.daemon = True
        thread.start()
        
    def stop_sorting(self):
        self.processing = False
        self.progress.stop()
        self.log_message("Process stopped by user")
        
    def test_single_image(self):
        if not self.project_path.get():
            messagebox.showerror("Error", "Please select a DeepDanbooru project folder")
            return
            
        file_path = filedialog.askopenfilename(
            title="Select Image to Test",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        
        if file_path:
            self.log_message(f"Testing image: {os.path.basename(file_path)}")
            tags = self.get_tags_for_image(file_path)
            self.display_image(file_path)
            self.display_tags(tags)
            
            classification = self.classify_image(tags)
            self.log_message(f"Classification: {classification}")
            
    def display_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.image_label.config(text=f"Error loading image: {str(e)}")
            
    def display_tags(self, tags):
        self.tags_text.delete(1.0, tk.END)
        if tags:
            for tag, score in tags.items():
                self.tags_text.insert(tk.END, f"{tag}: {score:.4f}\n")
        else:
            self.tags_text.insert(tk.END, "No tags found")
            
    def get_tags_for_image(self, image_path):
        try:
            cmd = [
                self.python_executable, "-m", "deepdanbooru", "evaluate", 
                image_path, 
                "--project-path", self.project_path.get()
            ]
            
            self.log_message(f"Running: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            
            if result.returncode != 0:
                self.log_message(f"Error: {result.stderr}")
                return {}
                
            tags = {}
            lines = result.stdout.split('\n')
            for line in lines:
                if '(' in line and ')' in line:
                    try:
                        parts = line.strip().split(') ')
                        if len(parts) >= 2:
                            score_str = parts[0].replace('(', '')
                            tag = parts[1].strip()
                            score = float(score_str)
                            tags[tag] = score
                    except:
                        continue
                        
            return tags
            
        except subprocess.TimeoutExpired:
            self.log_message("DeepDanbooru evaluation timed out")
            return {}
        except Exception as e:
            self.log_message(f"Error getting tags: {str(e)}")
            return {}
            
    def classify_image(self, tags):
        realistic_tags = ['realistic', 'photorealistic', 'real_life', 'photo']
        for tag in tags:
            if any(real_tag in tag.lower() for real_tag in realistic_tags):
                return "REAL"
        return "ANIME"
        
    def process_images(self):
        source_dir = self.source_folder.get()
        project_dir = self.project_path.get()
        dry_run = self.dry_run.get()
        
        anime_dir = os.path.join(source_dir, "anime")
        real_dir = os.path.join(source_dir, "real")
        
        if not dry_run:
            os.makedirs(anime_dir, exist_ok=True)
            os.makedirs(real_dir, exist_ok=True)
            
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        image_files = [
            f for f in os.listdir(source_dir) 
            if f.lower().endswith(image_extensions) and os.path.isfile(os.path.join(source_dir, f))
        ]
        
        total = len(image_files)
        self.log_message(f"Found {total} images to process")
        
        for i, filename in enumerate(image_files):
            if not self.processing:
                break
                
            file_path = os.path.join(source_dir, filename)
            self.log_message(f"Processing {i+1}/{total}: {filename}")
            
            self.root.after(0, lambda f=file_path: self.display_image(f))
            
            tags = self.get_tags_for_image(file_path)
            self.root.after(0, lambda: self.display_tags(tags))
            
            classification = self.classify_image(tags)
            self.log_message(f"Classified as: {classification}")
            
            if classification == "ANIME":
                dest_dir = anime_dir
            else:
                dest_dir = real_dir
                
            dest_path = os.path.join(dest_dir, filename)
            
            if not dry_run:
                counter = 1
                name, ext = os.path.splitext(filename)
                while os.path.exists(dest_path):
                    new_name = f"{name}_{counter}{ext}"
                    dest_path = os.path.join(dest_dir, new_name)
                    counter += 1
                    
                try:
                    shutil.move(file_path, dest_path)
                    self.log_message(f"Moved to: {dest_path}")
                except Exception as e:
                    self.log_message(f"Error moving file: {str(e)}")
            else:
                self.log_message(f"Would move to: {dest_path} (dry run)")
                
        self.processing = False
        self.root.after(0, self.progress.stop)
        self.root.after(0, lambda: self.log_message("Sorting completed!"))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DeepDanbooruSorter(root)
    root.mainloop()