import sys

from .filter import filter_file

if __name__ == "__main__":
    filter_file(sys.argv[1])