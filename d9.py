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

# Global variables
task="d9-t"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def a():
    rows = [n for n in readInput().split('\n')]
    res = 0

    print("A): ", res)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
