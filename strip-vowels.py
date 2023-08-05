#!/usr/bin/env python3

import argparse
import re

"""
Author: Kenny Kelley
Date: 2023-08-05

"""


def do_argparse():
    parser = argparse.ArgumentParser(
        description="Removes all of the vowels from the given strings."
    )
    parser.add_argument(
        "strings",
        metavar="string",
        help="a string you would like to have the vowels removed from",
        nargs="+",
    )
    return parser.parse_args()


def main():
    args = do_argparse()
    print(re.sub("[aeiouAEIOU]", "", " ".join(args.strings)))


if __name__ == "__main__":
    main()
