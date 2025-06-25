import os
import shutil
import logging

DOWNLOADS_PATH = r"C:\Users\HP\Downloads"
LOG_FILE_NAME = "organizer.log"
TEST_RUN = True

logging.basicConfig(
    filename=os.path.join(DOWNLOADS_PATH, LOG_FILE_NAME),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s" )

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Video": [".mp4", ".avi", ".mov", ".mkv"] }
OTHER_FOLDER = "Others"

def make_folder(path):
    if not os.path.exists(path):
        if TEST_RUN:
            print(f"[TEST-RUN] Would create folder: {path}")
        else:
            os.makedirs(path)
        logging.info(f"Created directory: {path}")

def figure_out_category(file_name):
    exit = os.path.splitext(file_name)[1].lower()
    for category_name, ext_list in CATEGORIES.items():
        if exit in ext_list:
            return category_name
    return OTHER_FOLDER

def move_file(file_name):
    old_path = os.path.join(DOWNLOADS_PATH, file_name)
    category = figure_out_category(file_name)
    new_folder = os.path.join(DOWNLOADS_PATH, category)  
    new_path = os.path.join(new_folder, file_name)
    
    make_folder(new_folder)
    if TEST_RUN:
        print(f"[TEST-RUN] Would move '{file_name}' to '{category}/'")
        logging.info(f"[TEST-RUN] Would move {file_name} to {category}/")
    try:
        shutil.move(old_path, new_path)
        logging.info(f"Moved file: {file_name} → {category}/")
    except Exception as e:
        logging.error(f"Could not move {file_name}: {e}")

def Clean_up_downloads():
    logging.info("Starts file sorting...")
    for file_name in os.listdir(DOWNLOADS_PATH):
        full_path = os.path.join(DOWNLOADS_PATH, file_name)
        if os.path.isfile(full_path):
            move_file(file_name)
    logging.info("All files are sorted!!")

if __name__ == "__main__":
    Clean_up_downloads()