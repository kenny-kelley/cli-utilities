#!/usr/bin/env python3

import argparse
from datetime import datetime

ARGUMENT_DESCRIPTION = "an RFC 3339 formatted date-time string"


def do_argparse():
    parser = argparse.ArgumentParser(
        description="Finds out the difference between two RFC 3339 formatted date-time strings."
    )
    parser.add_argument("a", help=ARGUMENT_DESCRIPTION, type=str)
    parser.add_argument("b", help=ARGUMENT_DESCRIPTION, type=str)
    return parser.parse_args()


def main():
    args = do_argparse()
    print(datetime.fromisoformat(args.b) - datetime.fromisoformat(args.a))


if __name__ == "__main__":
    main()
