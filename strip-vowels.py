#!/usr/bin/env python3

import argparse

"""
Author: Kenny Kelley
Date: 2020-08-31

"""


VOWELS = ("a", "e", "i", "o", "u")


def do_argparse():
    parser = argparse.ArgumentParser(
        description="Removes all of the vowels from a given string."
    )
    parser.add_argument(
        "input_str", help="a string you would like to have the vowels removed from"
    )
    return parser.parse_args()


def strip_vowels(input_str):
    output_str = ""
    for c in input_str:
        if c.lower() not in VOWELS:
            output_str += c
    return output_str


def main():
    args = do_argparse()
    print(strip_vowels(args.input_str))


if __name__ == "__main__":
    main()
