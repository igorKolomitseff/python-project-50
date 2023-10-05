#!/usr/bin/env python3
from gendiff.cli_parser import get_argparse
from gendiff.diff_generator import generate_diff


def main():
    first_file, second_file = get_argparse()

    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()
