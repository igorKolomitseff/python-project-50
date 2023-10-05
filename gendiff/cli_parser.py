import argparse


def get_argparse() -> tuple:
    """Allows the program to get the necessary arguments and track
            the correctness of their use.

    Returns:
        A tuple of passed arguments.
    """

    # creating an ArgumentParser object for parsing the command line into
    # Python data types
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    # adding positional arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # adding optional argument
    parser.add_argument('-f', '--format', help='set format of output')

    # parsing arguments
    args = parser.parse_args()

    return args.first_file, args.second_file
