#!/usr/bin/python -tt

import sys
import re
import itertools  # http://docs.python.org/library/itertools.html#itertools.combinations

# RULES
def addAll(args):
    val = ""
    for arg in args:
        val += "%i+" % arg
    return val[:-1]

def subAll(args):
    val = ""
    for arg in args:
        val += "%i-" % arg
    return val[:-1]

def multiplyAll(args):
    val = ""
    for arg in args:
        val += "%i*" % arg
    return val[:-1]

def divideAll(args):
    val = ""
    for arg in args:
        val += "%i/" % arg
    return val[:-1]
    
def testPatterns(args):
    # GENERATOR FOR TEST PATTERNS
    patterns = ['%i+%i+%i+%i',
                '%i-%i-%i-%i',
                '%i*%i*%i*%i',
                '%i/%i/%i/%i',
                '(%i+%i)*(%i+%i)',
                '(%i-%i)*(%i-%i)',
                '(%i+%i)*%i*%i',
                '(%i-%i)*%i*%i',
                '(%i-%i)*%i+%i',
                '(%i-%i)*%i-%i',
                '%i*(%i+%i)+%i',
                '%i*(%i-%i)-%i',
                '%i*(%i-%i)+%i',
                '%i*(%i+%i)-%i']
    for pattern in patterns:
        yield pattern % (int(args[0]), int(args[1]), int(args[2]), int(args[3]))

# GENERATE ALL POSSIBLE COMBINATIONS FROM ARGS PROVIDED
# Code based on the following documetion
# http://docs.python.org/library/itertools.html#itertools.combinations
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        yield tuple(pool[i] for i in indices)

# GAMEPLAY
def play24(ints):
    target = 24
    for int in ints:
        print int
    print "thinking..."

    for combo in combinations(ints, 4):
        print "COMBO:", combo
        for test in testPatterns(combo):
            print test
            if eval(test) == target:
                print "FOUND: ", test
                return
    print "no patterns result in %i" % target
    
# Define a main() function that prints a little greeting.
def main():
    ints = sys.argv[1:]
    if not ints:
        print "usage: [--int 1-10][--int 1-10][--int 1-10][--int 1-10]";
        # SET A DEFAULT PATTERN TO PLAY AGAINST
        ints = [4,10,4,2]
       
    for i in ints:
        if(i == 0): 
            print "no 0's please"
            sys.exit(1)
       
    if len(ints) > 4:
        print "only 4 arguments, please";
        sys.exit(1)
        
    play24(ints)
    print "end"

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()