import os
import shutil
import json
import time
import zipfile
import sys

from File import File
from Directory import Directory

def print_messages(func):
    def envelope(self):
        print("[auto-bkp]: Process started")
        print()
        backup_directory = Directory(func())
        print("[auto-bkp]: Finished process")
        print()
        print("Process resume:")
        print("Backup folder path:", backup_directory.src)
        print("Total backup size:", str(backup_directory.size()) + "MB")
    return envelope

class Backup:
    def __init__(self) -> None:
        self.ROOT = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(self.ROOT, "config.json")) as config_file:
            self.CONFIG = json.load(config_file)
        self.directories = self.CONFIG["dir"]
        self.files = self.CONFIG["file"]

    def new_backup_directory(self)->str:
        creation_destination_ls = os.listdir(self.CONFIG["creation_destination"])
        created = False
        backup_number = 0

        while not created:
            folder_name = "backup" + str(backup_number)
            if folder_name in creation_destination_ls:
                backup_number += 1
                continue
            os.mkdir(os.path.join(self.CONFIG["creation_destination"], folder_name))
            created = True

        return os.path.join(self.CONFIG["creation_destination"], "backup" + str(backup_number))

    def new_backup(self):
        backup_directory = self.new_backup_directory()

        for file in self.files:
            _file = File(file)
            display_size = str(_file.size()) + "MB"
            print("Creating copy of", _file.name, display_size)
            _file.copy(backup_directory)

        for directory in self.directories:
            _directory = Directory(directory)
            display_size = str(_directory.size()) + "MB"
            print("Compressing and making a copy of", _directory.name, display_size)
            _directory.compress(backup_directory)
