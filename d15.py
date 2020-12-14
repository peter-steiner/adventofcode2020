#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/15
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d15"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    print("B): ", rows)

def b():
    rows = [n for n in readInput().split('\n')]
    print("B): ", rows)

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    b()

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
