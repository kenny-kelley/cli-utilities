#!/usr/bin/env python3

import argparse
import os
import random
import sys


def do_argparse():
    parser = argparse.ArgumentParser(
        description="Generates a random integer.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-a",
        "--lower-bound",
        help="inclusive lower bound for RNG pool",
        type=int,
        default=0,
    )
    parser.add_argument(
        "-b",
        "--upper-bound",
        help="inclusive upper bound for RNG pool",
        type=int,
        default=sys.maxsize,
    )
    parser.add_argument(
        "--seed-size",
        help="size in bytes of the seed the OS generates via os.urandom()",
        type=int,
        default=1024,
    )
    return parser.parse_args()


def main():
    args = do_argparse()
    random.seed(a=os.urandom(args.seed_size), version=2)
    print(random.randint(args.lower_bound, args.upper_bound))


if __name__ == "__main__":
    main()
