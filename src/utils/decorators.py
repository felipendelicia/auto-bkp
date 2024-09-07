from src.Directory import Directory

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
        print("Total backup size:", str(backup_directory.size()) + "MB")
        print()
        print("Source code:", "github.com/felipendelicia/easy-backup", "♡")
    return envelope
