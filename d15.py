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
    numb = rows[0].split(",")
    
    #numb = "1,3,2".split(",")
    print(numb)
    numbers = ["X"]*2021
    for n in range(len(numb)):
        numbers[n] = int(numb[n])
    print("A): ", rows)
    turn = 0
    while turn < 2020:
        if numbers[turn] == "X":
            spoken = numbers[turn-1]
            if numbers.count(spoken) > 1: 
                indices = sorted([i for i, x in enumerate(numbers) if x == spoken], reverse=True)
                last, prev = indices[0:2]
                speak = last - prev
                numbers[turn] = speak
                #break
            else:
                numbers[turn] = 0
        turn += 1
    print(numbers[2019])

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
