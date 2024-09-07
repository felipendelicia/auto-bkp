import os
import zipfile
import shutil

from src.File import File

class Directory:
    def __init__(self, src:str) -> None:
        self.src = src
        self.name = os.path.basename(src)

    def size(self) -> float:
        total_size = 0
        if os.path.isfile(self.src):
            total_size = os.path.getsize(self.src)
        elif os.path.isdir(self.src):
            for dirpath, _, filenames in os.walk(self.src):
                for file in filenames:
                    filepath = os.path.join(dirpath, file)
                    total_size += os.path.getsize(filepath)
        return round(total_size / (1024 * 1024), 2)

    def compress(self, dest:str) -> None:
        archive_name = os.path.join(dest, self.name + ".zip")
        total_size = self.size()
        compressed_files = 0

        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            for ROOT, dirs, files in os.walk(self.src):
                for file in files:
                    _file = File(os.path.join(ROOT, file))

                    print(f"Compressed files: {compressed_files} | Current file: {_file.name} | File size: {_file.size()}MB")

                    zipf.write(_file.src, os.path.relpath(_file.src, os.path.join(self.src, '..')))

                    compressed_files += 1

            print(f"Compression completed successfully. Total compressed files: {compressed_files}")
        print()

    def delete(self):
        shutil.rmtree(self.src)
