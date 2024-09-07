import os
import sys

from src.Backup import Backup

class CLI:
    def run(self):
        while True:
            os.system("clear")

            print("easy-backup 0.1.0")
            print()
            print("1 - New backup")
            print("2 - Delete backups")
            print("3 - Edit config")
            print()

            option = input("Enter one option (1,2,3): ")
            exec = self.exect(option)

            if exec: break

    def exect(self, option):
        if option == "1":
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
