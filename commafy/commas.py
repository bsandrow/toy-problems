#!/usr/bin/env python
""" commas - Add comma separators to an integer """

import sys

def commas(i):
    try:
        i = int(i)
    except ValueError:
        sys.exit("Error: Not passed an integer.")

    n = 0
    while ( i / (1000 ** n) > 1000 ):
        n += 1
    n += 1

    get_segment = lambda n: i % (1000 ** n) / (1000 ** (n-1))

    return ','.join([
        str(get_segment(x)) for x in range(n, 0, -1)
    ])

if __name__ == '__main__':
    try:
        print commas(sys.argv[1])
    except ValueError:
        sys.exit("Error: Need to provide a number")
    except KeyboardError:
        sys.exit(">> Caught user interrupt. Exiting...")
