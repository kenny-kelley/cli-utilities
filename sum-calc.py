import argparse

"""
Author: Kenny Kelley
Date: 2020-04-22

"""


def do_argparse():
    parser = argparse.ArgumentParser(description='A calculator to sum up decimal, hexadecimal, and binary numbers.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input_mode', help='sets the mode of how values without prefixes should be interpretted', choices=['dec', 'hex', 'bin'], default='dec')
    parser.add_argument('-o', '--output_mode', help='sets the mode of the output value', choices=['dec', 'hex', 'bin'], default='dec')
    parser.add_argument('nums', metavar='num', help='a number to include in the sum', nargs='+')
    return parser.parse_args()


def main():

    args = do_argparse()
    teh_sum = 0
    for i in args.nums:
        if i.startswith('0x') or i.startswith('0X'):
            teh_sum += int(i, 16);
        elif i.startswith('0b') or i.startswith('0B'):
            teh_sum += int(i, 2)
        else:
            teh_sum += int(i)
            # TODO: consider input mode

    # TODO: find solution for inputing negative hex and bin values, parse_intermixed_args(...) and
    #   parse_known_args(...) are the best leads to look into

    if args.output_mode == 'hex':
        print(hex(teh_sum))
    elif args.output_mode == 'bin':
        print(bin(teh_sum))
    else:
        print(teh_sum)


if __name__ == '__main__':
    main()
