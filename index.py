import os
import shutil
import json
import time
import zipfile
import sys

with open('config.json') as config_file: CONFIG = json.load(config_file)
BKP_FOLDER_BASE_NAME = "backup"
ROOT = os.getcwd()

def get_archive_name_by_path(path):
    return os.path.basename(path)

def get_directories():
    return CONFIG["dir"]

def get_files():
    return CONFIG["file"]

def compress_dir(src, dest):
    archive_name = os.path.join(dest, get_archive_name_by_path(src) + ".zip")
    total_size = get_size(src)
    compressed_files = 0


    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
        for ROOT, dirs, files in os.walk(src):
            for file in files:
                file_path=os.path.join(ROOT, file)
                file_size = get_size(file_path)

                print(f"Compressed files: {compressed_files} | Current file: {file} | File size: {file_size}MB")

                zipf.write(file_path, os.path.relpath(file_path, os.path.join(src, '..')))

                compressed_files += 1

        print(f"Compression completed successfully. Total compressed files: {compressed_files}")
    print()



def copy_file(src, dest):
    shutil.copy(src, dest)

def create_bkp_dir():
    dir_ls = os.listdir()
    created = False
    bkp_number = 0

    while not created:
        folder_name = BKP_FOLDER_BASE_NAME + str(bkp_number)
        if folder_name in dir_ls:
            bkp_number += 1
            continue
        else:
            os.mkdir(f"./{folder_name}")
            created = True

    return BKP_FOLDER_BASE_NAME + str(bkp_number)

def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, _, filenames in os.walk(path):
            for file in filenames:
                filepath = os.path.join(dirpath, file)
                total_size += os.path.getsize(filepath)
    return round(total_size / (1024 * 1024), 2)

def print_messages(func):
    def envelope():
        print("[auto-bkp]: Process started")
        print()
        abs_bkp_folder = func()
        print("[auto-bkp]: Finished process")
        print()
        print("Process resume:")
        print("Backup folder path:", abs_bkp_folder)
        print("Total backup size:", str(get_size(abs_bkp_folder)) + "MB")
    return envelope

@print_messages
def main():
    bkp_folder = create_bkp_dir()
    abs_bkp_folder = os.path.join(ROOT, bkp_folder)
    files = get_files()
    dirs = get_directories()

    for file in files:
        size = str(get_size(file)) + "MB"
        print("Creating copy of", file, size)
        copy_file(file, abs_bkp_folder)

    for dir in dirs:
        size = str(get_size(dir)) + "MB"
        print("Compressing and making a copy of", dir, size)
        compress_dir(dir, abs_bkp_folder)

    return abs_bkp_folder

if __name__ == "__main__":
    main()
