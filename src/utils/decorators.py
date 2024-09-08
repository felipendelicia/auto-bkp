from src.Directory import Directory
from src.utils.format import display_size

def new_backup_decorator(func):
    def envelope(self, *args, **kwargs):
        print("Backup process started")
        print()
        backup_directory = func(self, *args, **kwargs)
        backup_directory = Directory(backup_directory)
        print("Backup ready!")
        print()
        print("Backup resume:")
        print("Backup folder path:", backup_directory.src)
        print("Total backup size:", display_size(backup_directory.size()))
    return envelope
