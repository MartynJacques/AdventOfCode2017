#!/env/bin/python
import sys
import argparse
import os


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile')
    return parser


def main(args):
    data = [line.strip('\n') for line in open(args.inputfile)]
    for seq in data:
        seq_l = len(seq)
        seq_half_l = seq_l / 2
        total = 0
        for i in range(0, seq_l):
            if seq[i] == seq[(i + seq_half_l) % seq_l]:
                total += int(seq[i])
        print total

if __name__ == '__main__':
    args = build_parser().parse_args()
    assert os.path.isfile(args.inputfile), 'Must provide a valid inputfile'
    main(args)
