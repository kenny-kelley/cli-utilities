import argparse

"""
Author: Kenny Kelley
Email: kelley.796@osu.edu
Date: 2019-17-12

"""


def do_argparse():
    arg_parser = argparse.ArgumentParser(description='Prints the number of unique strings '
        + 'separated by newlines in a file.')
    arg_parser.add_argument('file', help='path to a valid file')
    return arg_parser.parse_args()


def main():

    args = do_argparse()

    working_set = set()
    with open(args.file, 'r') as in_file:
        for line in in_file:
            if line != '\n': # Exclude empty lines
                working_set.add(line)

    print(len(working_set)) # Python accesses lengths for built-in types in constant time, bite me


if __name__ == '__main__':
    main()
