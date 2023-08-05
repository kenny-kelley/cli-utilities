#!/usr/bin/env python3

import argparse


def do_argparse():
    parser = argparse.ArgumentParser(description="Does absolutely nothing.")
    return parser.parse_args()


def main():
    args = do_argparse()
    # !TODO


if __name__ == "__main__":
    main()
