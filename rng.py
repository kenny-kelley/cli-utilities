#!/usr/bin/env python3

import argparse
import sys
import random
import os

"""
Author: Kenny Kelley
Date: 2019-12-18

"""


def do_argparse():
    parser = argparse.ArgumentParser(description='Generates a random integer.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a', '--start', help='inclusive lower bound for RNG pool', type=int, default=0)
    parser.add_argument('-b', '--stop', help='inclusive upper bound for RNG pool', type=int, default=sys.maxsize)
    parser.add_argument('--seed_size', help='size in bytes of the seed the OS generates via os.urandom()', default=1024)
    return parser.parse_args()


def main():
    args = do_argparse()
    random.seed(a=os.urandom(args.seed_size), version=2)
    print(random.randrange(args.start, args.stop))


if __name__ == '__main__':
    main()
