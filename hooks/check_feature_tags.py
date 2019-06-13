import argparse
import io
import sys

def remove_unwanted_tags(filename):
    # infile = "messy_data_file.txt"
    # outfile = "cleaned_file.txt"

    # delete_list = ["word_1", "word_2", "word_n"]
    # fin = open(infile)
    # fout = open(outfile, "w+")
    # for line in fin:
    #     for word in delete_list:
    #         line = line.replace(word, "")
    #     fout.write(line)
    # fin.close()
    # fout.close()
    with open(filename, 'r') as file:
        data = file.read().replace('@current', '')
    
    with open(filename, 'w') as file:
        file.write(data)

def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='feature filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        print('filename: ', filename)
        remove_unwanted_tags(filename)
        # try:
        #     with io.open(filename, 'rb') as xml_file:
        #         xml.sax.parse(xml_file, xml.sax.handler.ContentHandler())
        # except xml.sax.SAXException as exc:
        #     print('{}: Failed to xml parse ({})'.format(filename, exc))
        #     retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main())
