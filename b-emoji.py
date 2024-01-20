#!/usr/bin/env python3

import argparse
import re

B_EMOJI = "\U0001f171\ufe0f "
CONSONANTS_REGEX = "[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]"
B_REGEX = "[bB]"


def do_argparse():
    parser = argparse.ArgumentParser(description=B_EMOJI)
    parser.add_argument("strings", metavar="string", help=B_EMOJI, nargs="+", type=str)
    parser.add_argument(
        "-a",
        "--all-consonants",
        help=B_EMOJI,
        action="store_true",
    )
    return parser.parse_args()


def main():
    args = do_argparse()
    if args.all_consonants:
        print(re.sub(CONSONANTS_REGEX, B_EMOJI, " ".join(args.strings)))
    else:
        print(re.sub(B_REGEX, B_EMOJI, " ".join(args.strings)))


if __name__ == "__main__":
    main()
