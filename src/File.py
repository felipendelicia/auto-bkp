import os
import shutil

class File:
    def __init__(self, src:str) -> None:
        self.src = src
        self.name = os.path.basename(src)

    def size(self) -> float:
        return os.path.getsize(self.src)

    def copy(self, dest:str)->None:
        shutil.copy(self.src, dest)
