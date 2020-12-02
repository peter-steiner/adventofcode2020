#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/1
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d1"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0
    for row in rows:
        se = 2020 - row
        #print("expense: ", row, se)
        if se in rows:        
            print("expense: %d, %d", row, se)
            res = row * se
            break
    print("A): ", res)

def b():
    rows = [n for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
