#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FizzBuzz implementation"""

from __future__ import print_function
import argparse



def fizzbuzz(i):
    if i % 15 == 0:
        return 'FizzBuzz'
    elif i % 5 == 0:
        return 'Buzz'
    elif i % 3 == 0:
        return 'Fizz'
    else:
        return i


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, required=True,
                        help="1 <= n < 10000",
                        choices=range(1, 10000), metavar="[1-9999]")
    parser.add_argument('-m', action='store', type=int, required=True,
                        help="1 < m <= 10000",
                        choices=range(2, 10001), metavar="[2-10000]")
    args = parser.parse_args()
    n = args.n
    m = args.m
    if n < m:
        for i in range(n, m+1):
            print(fizzbuzz(i))
        # alternative:
        # for i in range(n, m+1):
        #    print("fizz"*(i % 3 == 0) + "buzz"*(i % 5 == 0) or i)
    else:
        raise argparse.ArgumentTypeError(
            "Min and Max must be in range 1 <= n < m <= 10000")


if __name__ == '__main__':
    main()