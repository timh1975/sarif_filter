import sys
from sarif_filter.filter import filter_file

# arguments

def main():
    if len(sys.argv) < 2:
        print("Error: No input file provided.")
        sys.exit(1)

    filename = sys.argv[1]
    rule = sys.argv[2]
    print(rule)
    filter_file(filename, rule)

if __name__ == "__main__":
    main()