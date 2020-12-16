#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/16
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d16-t"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    
    for row in rows:
        print(row)

    print("A): ")

def b():
    rows = [n for n in readInput().split('\n')]

    print("B): ")

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))
    
    b()
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    
    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
