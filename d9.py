#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/9
"""

# Imports
import sys
import os
import re
import math
import itertools

# Global variables
task="d9"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def a():
    nmbrs = [int(n) for n in readInput().split('\n')]
    res = 0

    preambleLength = 25
    preamble = []
    pos = preambleLength

    while pos < len(nmbrs):   
        #print("######")
        preamble = nmbrs[pos-preambleLength:pos]     
        result = list(itertools.combinations(preamble, 2))
        match = False
        for i in result:
            if sum(i) == nmbrs[pos]:
                #print(nmbrs[pos], i)
                match = True
        if not match:
            print(nmbrs[pos])

        pos += 1
    print("A): ", res)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
