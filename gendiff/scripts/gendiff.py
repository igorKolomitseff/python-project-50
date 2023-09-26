#!/usr/bin/env python3
import argparse

def main():
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



if __name__ == '__main__':
    main()