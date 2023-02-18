#!/usr/bin/env python3

import argparse

"""
Author: Kenny Kelley
Date: 2020-04-22

"""


def do_argparse():
    parser = argparse.ArgumentParser(description='A calculator to sum up decimal, hexadecimal, and binary numbers.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-o', '--output_mode', help='sets the mode of the output value', choices=['hex', 'bin', 'dec'], default='hex')
    parser.add_argument('-d', '--calc_diff', help='including this flag makes the calculator find the difference rather than the sum', action='store_true')
    parser.add_argument('nums', metavar='num', help='a well formed number to include in the calculation\n(Ex: \"0x2a\" or \"0b101010\" or \"42\"', nargs='+')
    return parser.parse_args()


# Parameters:
#   "a" is int and "b" is a str
def add(a, b):
    if b.lower().startswith('0x'):
        a += int(b, 16);
    elif b.lower().startswith('0b'):
        a += int(b, 2)
    else:
        a += int(b)
    return a


# Parameters:
#   "a" is int and "b" is a str
def subtract(a, b):
    if b.lower().startswith('0x'):
        a -= int(b, 16);
    elif b.lower().startswith('0b'):
        a -= int(b, 2)
    else:
        a -= int(b)
    return a


def main():

    args = do_argparse()
    teh_sum = 0
    if args.calc_diff:
        for i in args.nums:
            if args.nums.index(i) == 0:
                teh_sum = add(teh_sum, i)
            else:
                teh_sum = subtract(teh_sum, i)
    else:
        for i in args.nums:
            teh_sum = add(teh_sum, i)

    if args.output_mode == 'hex':
        print(hex(teh_sum))
    elif args.output_mode == 'bin':
        print(bin(teh_sum))
    else:
        print(teh_sum)


if __name__ == '__main__':
    main()
