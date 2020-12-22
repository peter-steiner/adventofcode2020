#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/22
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d22"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]

    p1 = []
    p2 = []
    
    p = []
    for row in rows:
        if "Player" in row:
            print("Reading p1")
        else:
            if len(row) == 0:
                p1 = p[:]
                p = []
            else:
                p.append(int(row))
    p2 = p[:]
    # Reverse and place deck on table
    p1 = p1[::-1]
    p2 = p2[::-1]

    print(p1)
    print(p2)
    stack = []
    winnerStack = []
    points = 0
    #for i in range(1, 10):
    i = 0
    while True:
        i += 1
        stack.append(p1.pop()) 
        stack.append(p2.pop()) 
        # C1 as default winner
        winner = "p1"
        # C2 wins
        ls = len(stack)
        if stack[ls-2] < stack[ls-1]:
            winner = "p2"

        #print("winner", winner, stack)
        if winner == "p1":  
            stack = stack[::-1]
        while len(stack) > 0:
            if winner == "p2":  
                p2.insert(0, stack.pop())
                p2.insert(0, stack.pop())
            else:
                p1.insert(0, stack.pop())
                p1.insert(0, stack.pop())
        #print("p1, p2\n-- Round ", i, " --\n", p1[::-1], p2[::-1])
        if not p1:
            print("Winner: P2", p2)
            winnerStack = p2[:]
            break
        if not p2:
            print("Winner: P1", p1)
            winnerStack = p1[:]
            break 
    
    for i in range(len(winnerStack)):
        points += (i+1)*winnerStack[i]  
    res = 0
    print("B): ", points)

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
