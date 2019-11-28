import argparse
import sys

def dos2unix(filename):
    # inspired from https://github.com/techtonik/dos2unix/blob/master/dos2unix.py
    content = ''
    with open(filename, 'rb') as infile:
        content = infile.read()
    with open(filename, 'wb') as output:
        for line in content.splitlines():
            output.write(line + b'\n')

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames dos2unix needs to apply to.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        dos2unix(filename)
    return retval


if __name__ == '__main__':
    sys.exit(main())
