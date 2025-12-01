# 📁 File Organizer 

A simple and elegant desktop application that automatically organizes files inside a selected folder into categorized subfolders.  
Built with **Python** and **Tkinter**, featuring a clean UI and an **Undo** option.

---

## ✨ Features

- ✔️ Automatically organizes files into categories  
- ✔️ Clean and modern Tkinter GUI  
- ✔️ Undo last organization action  
- ✔️ Supports images, videos, documents, audio, archives, code files, executables  
- ✔️ Customizable file-type categories  
- ✔️ No external libraries required  

---

## 📂 Supported File Categories

```python
FILE_TYPES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'],
    "Videos": ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    "Audio": ['.mp3', '.wav', '.m4a', '.aac', '.flac'],
    "Archives": ['.zip', '.rar', '.7zip', '.tar', '.gz'],
    "Code": ['.py', '.cpp', '.c', '.java', '.js', '.html', '.css', '.ts'],
    "Executables": ['.exe', '.msi', '.bat'],
}
```
---
## 🖥️ How It Works

1. Click **Browse Folder** and select the folder you want to organize.
2. Click **Organize Files**.
3. The application scans every file in the folder (ignoring directories).
4. Files are moved into automatically created category folders based on their extensions.
5. If a file doesn't match any known extension, it is placed in the **Others** folder.
6. You can click **Undo Changes** to revert all organized files back to their original locations.


---

## 📸 GUI Overview

The Tkinter GUI includes:
- Folder input field  
- Browse button  
- Organize button  
- Undo button  
- Clean card-style centered layout  

## 🎥 Demo

https://github.com/TaH00R/file_arranger/blob/main/demo.mkv

---

## 🧠 Code Overview

### `organize_folder(path)`
Moves files into categorized subfolders and logs movements in a history dictionary.

### `undo_changes()`
Restores all moved files back to their original locations.

### `select_folder()`
Opens a directory selection dialog and updates the input field.

### Tkinter UI
Creates:
- Main application window  
- Styled buttons  
- Entry field  
- Card-like container  
- Event bindings  

---

## 🚀 Running the Project

### 1. Make sure Python 3.x is installed  
Tkinter is included by default on most systems.

### 2. Run the script  

---

## 🔧 Requirements

- Python 3.x  
- Tkinter  

No external libraries required.

---

## 🛠️ Future Enhancements

- Dark mode support  
- Drag-and-drop folder selection  
- Custom user-defined categories  
- Progress bar while organizing  
- Save category settings  

---

## 🤝 Contributing

Feedback and contributions are welcome!  
You can open issues or submit pull requests to improve this project.

---

## ⭐ Support

If you find this useful, consider giving the project a **star ⭐**!




