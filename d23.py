#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/23
"""

# Imports
import sys
import os
import re
import math
import time
from collections import deque

# Global variables
task="d23"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]

    cups = [int(n) for n in list(rows[0])]
    for k in range(1, 101):
        currentCup = cups[0]
        print("\n-- move ", k, " --")
        print("Current cup", currentCup)
        print("cups: ", cups)
        # Pick up cups
        index = 1
        circleLength = len(cups)
        pickedUpCups = []
        if circleLength > (index+4): 
            pickedUpCups = cups[index:index+3]
            cups = cups[0:index] + cups[index+3:]
        else:
            # left in arr end
            p1Prim = circleLength-1 - index
            p2Prim = 3-p1Prim
            pickedUpCups = cups[index:p1Prim] + cups[0:p2Prim]
            cups = cups[p2Prim:index]
        print("Pick up: ", pickedUpCups)
        maxCup = max(cups)
        minCup = min(cups)

        d=deque(cups)
        d.rotate(-1)
        cups = list(d)

        n = 1
        placeVal = maxCup
        while True:
            testCup = currentCup-n
            if testCup in cups:
                placeIndex = cups.index(testCup) 
                print("Pick up: ", pickedUpCups)
                print("Destination", testCup)
                # Revert - iterate - insert
                for c in pickedUpCups[::-1]:
                    cups.insert(placeIndex+1, c)
                break
            else:
                if testCup < minCup:
                    print("Destination", maxCup)
                    placeIndex = cups.index(maxCup) 
                    # Revert - iterate - insert
                    for c in pickedUpCups[::-1]:
                        cups.insert(placeIndex+1, c)
                    break
            n += 1
    ind = cups.index(1)
    d=deque(cups)
    d.rotate(-1*ind)
    cups = list(d)
    print("A): ", ''.join([str(x) for x in (cups[1:])]))

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
