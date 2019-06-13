import argparse
import io
import sys


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='feature filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        print('filename: ', filename)
        # try:
        #     with io.open(filename, 'rb') as xml_file:
        #         xml.sax.parse(xml_file, xml.sax.handler.ContentHandler())
        # except xml.sax.SAXException as exc:
        #     print('{}: Failed to xml parse ({})'.format(filename, exc))
        #     retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main())
