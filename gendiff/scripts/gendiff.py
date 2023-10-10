#!/usr/bin/env python3
from gendiff.cli_parser import get_argparse
from gendiff.diff_generator import generate_diff


def main():
    args = get_argparse()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format

    diff = generate_diff(first_file, second_file, formatter)
    print(diff)


if __name__ == '__main__':
    main()
