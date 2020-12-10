#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/11
"""

# Imports
import sys
import os
import re
import math
import itertools

task="d11"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def a():
    ratings = [int(n) for n in readInput().split('\n')]
    res = 0
    print("A): ", res)


def b():
    ratings = [int(n) for n in readInput().split('\n')]
    res = 0
    print("B):", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
