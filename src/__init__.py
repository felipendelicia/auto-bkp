import sys

from CLI import CLI

if __name__ == "__main__":
    cli = CLI(sys.argv[1:]) # First arg is a path
    cli.run()
