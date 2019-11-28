import argparse
import re
import sys

def remove_unwanted_tags(filename):
    with open(filename, 'r') as file:
        data = re.sub(r'@(current|focus)', '', file.read())
    
    with open(filename, 'w') as file:
        file.write(data)

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Feature filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        remove_unwanted_tags(filename)
    return retval


if __name__ == '__main__':
    sys.exit(main())
