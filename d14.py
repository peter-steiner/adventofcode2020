#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/6
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d6-t"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    #rows = [int(n) for n in readInput().split('\n')]
    res = 0
    n = 0
    p = 0
    prev = 0
    diff = []
    while p < 20:
        if (n+37)%457 == 0 and (n+68)%431 == 0:
            print(n)
            diff.append(abs(prev-n))
            prev = n
            p += 1
        n +=1
    
    for d in diff:
        print(diff)

    n = 0
    p = 0
    prev = 0
    diff = []
    while p < 20:
        if (n+3)%1889 == 0 and (n)%1789 == 0:
            print(n)
            diff.append(abs(prev-n))
            prev = n
            p += 1
        n +=1
    
    for d in diff:
        print(diff)

    print("A): ", res)

def b():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
