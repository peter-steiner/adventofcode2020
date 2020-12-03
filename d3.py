#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/3
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

def calc_multiplier(rows, slope):
    length = len(rows) * slope[0]
    act_length = len(rows[0])
    return math.ceil(length / act_length) + 1

def getTreesCountForSlope(rows, slope):

    multiplier = calc_multiplier(rows, slope)
    it = len(rows)

    forest = []
    for slot in rows:
        ext_slot = ""
        for n in range(multiplier):
            ext_slot += slot
        forest.append(list(ext_slot))

    step = slope[1]
    x = slope[0]
    trees = 0
    while step < it:
        slot = forest[step][x]
        forest[step][x] = "O"
        if slot == "#":
            trees += 1
            forest[step][x]
            forest[step][x] = "X"        
        step += slope[1]
        x += slope[0]

    #printForest(forest)
    return trees

def a():
    rows = [n for n in readInput().split('\n')]

    trees = getTreesCountForSlope(rows, [3,1])
    print("A): ", trees)

def b():
    rows = [n for n in readInput().split('\n')]
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]] 

    slopeTrees = 1
    for slope in slopes:
        slopeTrees *= getTreesCountForSlope(rows, slope)
        #print(getTreesCountForSlope(rows, slope))

    print("B): ", slopeTrees)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
