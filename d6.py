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
task="d6"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    res = 0

    groups = []
    g = ""
    for row in rows:
        print(row)
        g += row
        if len(row) == 0:
            groups.append(g)
            g = ""

    for group in groups:
        g = "".join(set(group))
        res += len(g)

    print("A): ", res)

def b():
    rows = [n for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
