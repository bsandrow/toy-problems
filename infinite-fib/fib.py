#!/usr/bin/env python
""" An infinite fibonacci sequence generator """

import itertools

def fib_generator():
    yield 0
    yield 1
    last = (0,1)
    while (True):
        value = last[0] + last[1]
        yield value
        last = (last[1], value)

fib_cache = []
generator = fib_generator()

def fib(n):
    global fib_cache
    global generator

    if n < 1:
        raise IndexError()
    elif n <= len(fib_cache):
        return fib_cache[n-1]
    else:
        fib_cache += [ x for x in itertools.islice(generator, 0, n - len(fib_cache)) ]
        return fib_cache[n-1]

if __name__ == '__main__':
    import sys

    try:
        try:
            args = sys.argv[1:]
            args.sort()
        except IndexError:
            sys.exit("Error: Did not provide a number to convert")

        try:
            args = map(int, args)
        except ValueError, e:
            sys.exit("Error: Could not convert '%s' to an int." % str(e))


        if len(args) > 1:
            print "Fibonacci Sequence %s: %s" % (
                "[n=" + ",".join(map(str, args)) + "]",
                ",".join(map(lambda x: str(fib(x)), args)),
            )
        else:
            print "Fibonacci Sequence #%d: %d" % (n, fib(n))
    except KeyboardInterrupt:
        sys.exit(">> Caught user interrupt. Exiting...")
