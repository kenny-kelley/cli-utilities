#!/usr/bin/env python3

import argparse

"""
Author: Kenny Kelley
Date: 2020-08-31

"""


def do_argparse():
    parser = argparse.ArgumentParser(description="wHat Do yOU tHiNk iT DOes?")
    parser.add_argument("string", help="a string you would like to memeify")
    return parser.parse_args()


def memeify(my_str):
    result = ""
    for char in my_str:
        ""


def main():
    args = do_argparse()
    print(memeify(args.string))


if __name__ == "__main__":
    main()
