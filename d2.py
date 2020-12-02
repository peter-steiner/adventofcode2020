#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/2
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d2"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    pws = [n for n in readInput().split('\n')]
    count = 0
    for row in pws:
        criteria, pw = row.split(sep:=":")
        occurance, char = criteria.split(" ")
        mino, maxo = [int(n) for n in occurance.split("-")]

        occurance_real = pw.count(char)
        if occurance_real >= mino and occurance_real <= maxo:            
#            print("row", row, criteria, pw, occurance, char)
            print("occurance, char", occurance_real, char, mino, maxo, pw)
            count += 1

    print("A): ", count)

def b():
    items = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
