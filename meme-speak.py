#!/usr/bin/env python3

import argparse
import random

"""
Author: Kenny Kelley
Date: 2023-02-18

"""


def do_argparse():
    parser = argparse.ArgumentParser(description="wHat Do yOU tHiNk iT DOes?")
    parser.add_argument(
        "strings",
        metavar="string",
        help="a string you would like to memeify",
        nargs="+",
    )
    return parser.parse_args()


def memeify(my_str: str) -> str:
    char_list = list(my_str)
    for i, char in enumerate(char_list):
        if i > 2:
            if (
                random.randint(0, 1) == 0
                and char_list[i - 1].isupper()
                or char_list[i - 2].isupper()
            ):
                char_list[i] = char.lower()
            else:
                char_list[i] = char.upper()
        else:
            if random.randint(0, 1) == 0:
                char_list[i] = char.lower()
            else:
                char_list[i] = char.upper()
    return "".join(char_list)


def main():
    args = do_argparse()
    print(memeify(" ".join(args.strings)))


if __name__ == "__main__":
    main()
