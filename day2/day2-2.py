#!/env/bin/python
import sys
import argparse
import os


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile')
    return parser


def main(args):
    data = [
        line.strip('\n').split() for line in open(args.inputfile)
    ]
    checksum = 0
    result = 0
    for row in data:
        row = [int(a) for a in row]
        for num in row:
            for other in row:
                if other != num:
                    if num % other == 0:
                        result += num / other

    print result

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert os.path.isfile(args.inputfile), 'Must provide a valid inputfile'
    main(args)
