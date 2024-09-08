import os
import sys

from src.Backup import Backup

class CLI:
    def run(self):
        while True:
            print("easy-backup 0.1.0\n\n1 - New backup\n2 - Delete backups\n3 - Edit config\n\nSource code: github.com/felipendelicia/easy-backup ♡") #CLI OPTIONS
            print()
            option = input("Enter one option [1, 2, 3] (Default 1): ")
            print()
            exec = self.exect(option)

            if exec: break

    def exect(self, option):
        if option == "1" or option == "":
            backup = Backup()
            backup.new_backup()
            return True

        elif option == "2":
            backup = Backup()
            backup.delete_backups()
            return True

        elif option == "3":
            os.system("nano " + os.path.join(os.path.dirname(sys.argv[0]), "./src/config.json"))
            return True

        return False
