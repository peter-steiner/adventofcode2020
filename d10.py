#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/10
"""

# Imports
import sys
import os
import re
import math
import itertools

# Global variables
task="d10"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def a():
    ratings = [int(n) for n in readInput().split('\n')]
    res = 0
    ratings.sort()
    ratings.insert(0, 0)
    ratings.append(max(ratings)+3)
    
    oneDiff = 0
    threeDiff = 0
    joltdiffs = []

    for i in range(len(ratings)-1):
        r = ratings[i]
        n = ratings[i+1]
        diff = n - r
        if diff <= 3:
            joltdiffs.append(diff)
        else:
            print("break at: ", i, n)
            break
    oneDiff = joltdiffs.count(1) 
    threeDiff = joltdiffs.count(3)
    res = oneDiff*threeDiff
    print("A): ", res)

globalDiff = 0

def validateDiff(ratings, pos, posPrim, ratingsPath):
    global globalDiff
  
    if posPrim == len(ratings)-1:
        r = ratings[pos]  
        n = ratings[posPrim]
        diff = n-r
        if diff >= 0 and diff <= 3:
            ratingsPath += " " + str(ratings[len(ratings)-2])
            ratingsPath += " " + str(ratings[len(ratings)-1])
            globalDiff += 1
            return 
    if posPrim > len(ratings)-1:
        return 

    r = ratings[pos]  
    n = ratings[posPrim]
    diff = n-r
    if diff >= 0 and diff <= 3:
        validateDiff(ratings, posPrim, posPrim+1, ratingsPath + " " + str(r))
        validateDiff(ratings, posPrim, posPrim+2, ratingsPath + " " + str(r))
        validateDiff(ratings, posPrim, posPrim+3, ratingsPath + " " + str(r))
    return


def b():
    ratings = [int(n) for n in readInput().split('\n')]

    global globalDiff
    globalDiff = 0
    ratings.insert(0, 0)
    ratings.append(max(ratings)+3)
    ratings.sort()

    ratingsPath = ""
    si = 0
    subArr = []
    for n in range(len(ratings)-1):
        if n < len(ratings)-1 and ratings[n+1] - ratings[n] == 3:
            subArr.append(ratings[si: n+1])
            si = n+1

    result = 1
    for arr in subArr:
        validateDiff(arr, 0, 1, ratingsPath)
        validateDiff(arr, 1, 2, ratingsPath)
        validateDiff(arr, 2, 3, ratingsPath)
        if globalDiff > 0:
            result *= globalDiff
        globalDiff = 0
    print(ratings)

    print("B):", result)

# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
