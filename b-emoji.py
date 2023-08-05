#!/usr/bin/env python3

import argparse
import re

B_EMOJI = "\U0001f171\ufe0f "


def do_argparse():
    parser = argparse.ArgumentParser(description=B_EMOJI)
    parser.add_argument("strings", metavar="string", help=B_EMOJI, nargs="+", type=str)
    return parser.parse_args()


def main():
    args = do_argparse()
    print(re.sub("[bB]", B_EMOJI, " ".join(args.strings)))


if __name__ == "__main__":
    main()
