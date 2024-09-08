import os
import shutil
import json
import time
import zipfile
import sys

from src.File import File
from src.Directory import Directory
from src.utils.decorators import new_backup_decorator
from src.utils.json import import_json
from src.utils.format import display_size

class Backup:
    def __init__(self) -> None:
        self.ROOT = os.path.dirname(os.path.abspath(__file__))
        self.CONFIG = import_json(os.path.join(self.ROOT, "config.json"))
        self.directories = self.CONFIG["dir"]
        self.files = self.CONFIG["file"]

    def _new_backup_directory(self)->str:
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

    def _backup_files(self, backup_directory:str):
        for file in self.files:
            _file = File(file)
            print("Creating copy of", _file.name, display_size(_file.size()))
            _file.copy(backup_directory)

    def _backup_dirs(self, backup_directory:str):
        for directory in self.directories:
            _directory = Directory(directory)
            print("Compressing and making a copy of", _directory.name, display_size(_directory.size()))
            _directory.compress(backup_directory)

    @new_backup_decorator
    def new_backup(self):
        backup_directory = self._new_backup_directory()
        self._backup_files(backup_directory)
        self._backup_dirs(backup_directory)
        return backup_directory

    def delete_backups(self):
        creation_destination_ls = os.listdir(self.CONFIG["creation_destination"])

        for i in range(50):
            current_backup_name = "backup" + str(i)
            if  current_backup_name in creation_destination_ls:
                dir = Directory(os.path.join(self.CONFIG["creation_destination"], current_backup_name))
                print("Erasing", dir.name, display_size(dir.size()))
                dir.delete()

        print("All backups were deleted.")
