#!/usr/bin/env python3

import argparse

"""
Author: Kenny Kelley
Date: 2023-02-18

"""


def do_argparse() -> argparse.Namespace:
    """Parses, validates, and provides feedback on command line arguments."""
    parser = argparse.ArgumentParser(
        description="A calculator to sum up binary, octal, decimal, and hexadecimal integers.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--output_base",
        help="sets the base of the output value",
        choices=["bin", "oct", "dec", "hex"],
        default="hex",
    )
    parser.add_argument(
        "-d",
        "--calc_diff",
        help="including this flag makes the calculator find the difference rather than the sum",
        action="store_true",
    )
    parser.add_argument(
        "nums",
        metavar="num",
        help='a well formed number to include in the calculation (Ex: "0b101010" or "0o777" or "42" or "0x2a")',
        nargs="+",
    )
    return parser.parse_args()


def convert_str_to_int(num: str) -> int:
    """Converts a string representation of a binary, octal, decimal, or hexadecimal integer to a decimal integer."""
    if num.lower().startswith("0b"):
        return int(num, 2)
    elif num.lower().startswith("0o"):
        return int(num, 8)
    elif num.lower().startswith("0x"):
        return int(num, 16)
    else:
        return int(num)


def find_result(nums: list, calc_diff: bool) -> int:
    """Finds the sum or difference of the given list of integers."""
    result = 0
    for i, num in enumerate(nums):
        if i == 0 or not calc_diff:
            result += convert_str_to_int(num)
        else:
            result -= convert_str_to_int(num)
    return result


def print_result(result: int, output_base: str) -> None:
    """Prints the binary, octal, decimal, or hexadecimal representation of the result."""
    if output_base == "bin":
        print(bin(result))
    elif output_base == "oct":
        print(oct(result))
    elif output_base == "hex":
        print(hex(result))
    else:
        print(result)


def main() -> None:
    args = do_argparse()
    result = find_result(args.nums, args.calc_diff)
    print_result(result, args.output_base)


if __name__ == "__main__":
    main()
