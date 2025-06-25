# GextonPython-Intern_Task06
File Organization Script Organize Your Downloads Folder by File Type

# 📂 File Organizer Script

This is a simple Python script that organizes your `Downloads` folder by moving files into subfolders like `images`, `documents`, `videos`, and `others`. It also supports a **dry-run mode** so you can preview the changes before actually moving any files.

---

## 🎯 Features
- ✅ Moves files into category-based folders.
- ✅ Creates subfolders if they don’t exist.
- ✅ Keeps a log of all file moves (`organizer.log`).
- ✅ Dry-run mode to preview file movements without making changes.

---

## 🛠️ Getting Started

### 1️⃣ Prerequisites
- Python 3.x installed.

### 2️⃣ Setup
1. Download or clone the project.
2. Open the `file_organizer.py` file.
3. Set the `DOWNLOADS_PATH` variable to your Downloads folder:
   ```python
   DOWNLOADS_PATH = r"C:\Users\YourUser\Downloads"
