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
    expenses = [int(n) for n in readInput().split('\n')]
    res = 0
    for row in expenses:
        se = 2020 - row
        #print("expense: ", row, se)
        if se in expenses:        
            print("expense: %d, %d", row, se)
            res = row * se
            break
    print("A): ", res)

def b():
    expenses = [int(n) for n in readInput().split('\n')]
    res = 0
    for exp in expenses:
        for exp_b in expenses:
            se = 2020 - exp
            if se < 2020:
                se = 2020 - exp - exp_b
                if se >= 0 and se in expenses:        
                    print("expense: %d, %d", exp, exp_b, se)
                    res = exp * exp_b * se
                    break
        if res > 0:
            break
        
    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
