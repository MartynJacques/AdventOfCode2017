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
    for row in data:
        row = [int(a) for a in row]
        diff = max(row) - min(row)
        checksum += diff
    print checksum

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert os.path.isfile(args.inputfile), 'Must provide a valid inputfile'
    main(args)
