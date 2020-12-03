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
task="d3"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def printForest(forest):
    for slot in forest:
        print("".join(slot)) 

def calc_multiplier(rows):
    length = len(rows) * 3
    act_length = len(rows[0])
    return math.ceil(length / act_length) + 1

def a():
    rows = [n for n in readInput().split('\n')]
    count = 0

    multiplier = calc_multiplier(rows)
    it = len(rows)
    print("Multiplier", multiplier)

    forest = []
    for slot in rows:
        ext_slot = ""
        for n in range(multiplier):
            ext_slot += slot
        forest.append(list(ext_slot))

    #print("rad 0", forest[0])
    step = 1
    x = 3
    trees = 0
    while step < it:
        slot = forest[step][x]
#        print("slot", slot, step, x)
 #       print("rad", forest[step])
        forest[step][x] = "O"
        if slot == "#":
            trees += 1
  #          print(forest[step][x])
            forest[step][x]
            forest[step][x] = "X"        
        step += 1
        x += 3

    printForest(forest)


    print("A): ", trees)

def b():
    rows = [n for n in readInput().split('\n')]
    count = 0
    print("B): ", count)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
