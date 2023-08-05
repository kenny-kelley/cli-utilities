#!/usr/bin/env python3

import argparse

"""
Author: Kenny Kelley
Date: 2019-12-17

"""


def do_argparse():
    parser = argparse.ArgumentParser(
        description="Prints the number of unique strings "
        + "separated by newlines in a file."
    )
    parser.add_argument("file", help="path to a valid file")
    return parser.parse_args()


def main():
    args = do_argparse()

    working_set = set()
    with open(args.file, "r") as in_file:
        for line in in_file:
            if line != "\n":  # Exclude empty lines
                working_set.add(line)

    # Python accesses lengths for built-in types in constant time, bite me
    print(len(working_set))


if __name__ == "__main__":
    main()
