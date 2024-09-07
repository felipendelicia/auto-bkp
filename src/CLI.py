import os

from Backup import Backup

class CLI:
    def __init__(self, args:list[str]):
        self.args = args

    def edit_configuration(self):
        src_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(src_path, "config.json")
        os.system("nano " + config_path)

    def new_backup(self):
        backup = Backup()
        backup.new_backup()

    def run(self):
        if len(self.args) == 0: self.new_backup()
        elif self.args[0] == "config": self.edit_configuration()
        else: print("Unknown command")
