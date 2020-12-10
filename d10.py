#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/10
"""

# Imports
import sys
import os
import re
import math
import itertools

# Global variables
task="d10"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def a():
    ratings = [int(n) for n in readInput().split('\n')]
    res = 0
    ratings.sort()
    ratings.insert(0, 0)
    ratings.append(max(ratings)+3)
    
    oneDiff = 0
    threeDiff = 0
    joltdiffs = []

    for i in range(len(ratings)-1):
        r = ratings[i]
        n = ratings[i+1]
        diff = n - r
        if diff <= 3:
            joltdiffs.append(diff)
        else:
            print("break at: ", i, n)
            break
    oneDiff = joltdiffs.count(1) 
    threeDiff = joltdiffs.count(3)
    res = oneDiff*threeDiff
    print("A): ", res)

def b():
    nmbrs = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)


# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
