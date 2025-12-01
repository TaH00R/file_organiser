import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

FILE_TYPES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp'],
    "Videos": ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
    "Audio": ['.mp3', '.wav', '.m4a', '.aac', '.flac'],
    "Archives": ['.zip', '.rar', '.7zip', '.tar', '.gz'],
    "Code": ['.py', '.cpp', '.c', '.java', '.js', '.html', '.css', '.ts'],
    "Executables": ['.exe', '.msi', '.bat'],
}

history = {}

def organize_folder(path):
    if not path:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    history.clear()

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)

                new_path = os.path.join(folder_path, filename)
                shutil.move(file_path, new_path)

                # Save movement info
                history[new_path] = file_path
                moved = True
                break

        if not moved:
            other_path = os.path.join(path, "Others")
            os.makedirs(other_path, exist_ok=True)

            new_path = os.path.join(other_path, filename)
            shutil.move(file_path, new_path)

            history[new_path] = file_path

    messagebox.showinfo("Success", "Files organized successfully!")

def undo_changes():
    if not history:
        messagebox.showinfo("Undo", "There is nothing to undo.")
        return

    for new_path, original_path in history.items():
        if os.path.exists(new_path):
            shutil.move(new_path, original_path)

    history.clear()
    messagebox.showinfo("Undo", "Changes reverted successfully!")

def select_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)


root = tk.Tk()
root.title("File Organizer")
root.geometry("500x350")
root.configure(bg="#f3f4f6")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 11),
    padding=8,
    background="#4CAF50",
    foreground="white"
)
style.map("TButton", background=[("active", "#45a049")])

card = tk.Frame(root, bg="white", padx=20, pady=20, bd=2, relief="groove")
card.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(card, text="📁 File Organizer", font=("Segoe UI", 16, "bold"), bg="white")
title.pack(pady=(0, 15))

folder_var = tk.StringVar()

entry = ttk.Entry(card, textvariable=folder_var, width=45, font=("Segoe UI", 10))
entry.pack()

browse_btn = ttk.Button(card, text="Browse Folder", command=select_folder)
browse_btn.pack(pady=10)

organize_btn = ttk.Button(card, text="Organize Files", command=lambda: organize_folder(folder_var.get()))
organize_btn.pack(pady=10)

undo_btn = ttk.Button(card, text="Undo Changes", command=undo_changes)
undo_btn.pack(pady=10)

root.mainloop()
