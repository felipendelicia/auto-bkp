import os
import shutil

class File:
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

    def copy(self, dest:str)->None:
        shutil.copy(self.src, dest)
