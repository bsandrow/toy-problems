#!/usr/bin/env python
""" letter-perms.py - Take a string of whole numbers, and return a list of possible translations. """

def getc(n):
    n = int(n)
    if n >= 1 and n <= 26:
        return chr(96 + n)
    else:
        return None

def f(s):
    if len(s) > 1:
        pairs = [ (getc(s[0]), s[1:]), (getc(s[:2]), s[2:]) ]
        return [ x[0] + y for x in pairs for y in f(x[1]) if x[0] ]
    elif len(s) == 1:
        return filter(lambda x: x, [ getc(s[0]) ])
    elif len(s) < 1:
        return ['']

if __name__ == '__main__':
    import sys
    import pprint
    pprint.pprint(f(sys.argv[1]))
