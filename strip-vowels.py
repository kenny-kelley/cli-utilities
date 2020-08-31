import argparse

"""
Author: Kenny Kelley
Date: 2020-08-31

"""


def do_argparse():
    parser = argparse.ArgumentParser(description='Removes all of the vowels from a given string.')
    parser.add_argument('string', help='a string you would like to have the vowels removed from')
    return parser.parse_args()


def strip_vowels(my_str):
    return my_str


def main():
    args = do_argparse()
    print(strip_vowels(args.string))


if __name__ == '__main__':
    main()
