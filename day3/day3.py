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
        line.strip('\n') for line in open(args.inputfile)
    ]
    for row in data:
        

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert os.path.isfile(args.inputfile), 'Must provide a valid inputfile'
    main(args)
