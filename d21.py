#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/21
"""

# Imports
import sys
import os
import re
import math
import time
import collections

# Global variables
task="d21"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    ingrUnique = set()
    ingredients = []
    ingrDict = dict()
#    allergensDict = dict()
    # Collect
    for row in rows:
        if "(contains" in row:  
            tmp, allergens = row.split(" (contains ")
            allergens = allergens[:-1]
            if ", " in allergens:
                allergens = allergens.split(", ")
            else: 
                allergens = [allergens]
            tmp = tmp.split(" ")
            for t in tmp:
                ingrUnique.add(t)
            ingredients += tmp
            for a in allergens:
                if a not in ingrDict:
                    ingrDict[a] = tmp[:]
                else:
                    ingrDict[a] += tmp[:]

    for a in ingrDict:
        ingrDict[a].sort()

    # Reduce
    newDict = dict()
    for l in ingrDict:
        duplicates = [item for item, count in collections.Counter(ingrDict[l]).items() if count > 1]
        count = [count for item, count in collections.Counter(ingrDict[l]).items() if count > 1]
        if len(count) > 0:
            maxC = max(count)
            ml = []
            newDict[l] = []
            for i in range(len(count)):
                c = count[i]
                if c == maxC:
                    ml.append(c)
                    newDict[l].append(duplicates[i])
            #print(max(count), ml)
        else:
            newDict[l] = ingrDict[l]
    matches = dict()
    # Match
    ingrDict = newDict
    for i in range(5):
        for l in ingrDict:          
            if len(ingrDict[l]) == 1:
                ingr = ingrDict[l][0]
                matches[l] = ingr
                if ingr in ingrUnique:
                    ingrUnique.remove(ingr)
                for i in ingrDict:
                    if ingr in ingrDict[i]:
                        ingrDict[i].remove(ingr)

    # Collect and sort alla ingredient/ allergen pairs
    sortedAllergens = list(matches.keys())    
    sortedAllergens.sort()
    resultB = ""
    for sa in sortedAllergens:
        resultB += matches[sa] + ","
    resultB = resultB[:-1]
    print("Result B:", resultB)

    sum = 0
#    print(ingredients)
    for k in ingrUnique:
        sum += ingredients.count(k)

    #print(ingrUnique)   
    print("Result A: ", sum)

def b():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

    """
    b()
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
    """

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
