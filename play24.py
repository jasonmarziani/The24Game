#!/usr/bin/python -tt

import sys
import re
import itertools  # http://docs.python.org/library/itertools.html#itertools.combinations

# GENERATOR FOR TEST PATTERNS
def testPatterns(args):
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
    

def main():
    ints = sys.argv[1:]
    
    # IF NO ARGS PASSED, DEFINE A DEFAULT SET
    if not ints:
        print "usage: [--int 1-10][--int 1-10][--int 1-10][--int 1-10]";
        ints = [4,10,4,2]
    
    # MAKE SURE THERE ARE NO 0'S SO WE DON'T GET A DENOMINATOR ERROR
    for i in ints:
        if(i == 0): 
            print "no 0's please"
            sys.exit(1)
    
    # MAKE SURE WE'VE GOT 4 AND ONLY 4 ARGUMENTS  
    if len(ints) != 4:
        print "only 4 arguments, please";
        sys.exit(1)
        
    play24(ints)
    print "end"

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()