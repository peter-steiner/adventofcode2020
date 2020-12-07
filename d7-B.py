#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/7
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d7"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def buildBagTree(bags, name, count, references):
    # is empty
    if len(references) == 0:
        return count

    #visit children if not already visited
    tmpCount = 0
    for ref in references:
        c1, bagName = ref.split("#")
        c2 = buildBagTree(bags, bagName, int(c1), bags[bagName])
        # First level doens't count
        if count == 0:
            tmpCount += c2
        else:
            # Multiply by number of containers
            tmpCount += count*c2
    # Add number of bags at current level
    tmpCount += count
#    print("C: {} N: {} P: {}".format(tmpCount, name, path))
    return tmpCount

def a():
    rows = [n for n in readInput().split('\n')]

    bags = {}
    # Parse bags and relations
    for row in rows:
        bagName, contain, holds = re.split("(bag[s]* contain )", row)
        bagName = bagName.replace(" ", "")
        
        bagsRel = []
        if "no other bags." not in holds:
            relBags = holds.split(", ")
            for b in relBags:
                #cleanup
                rawBagStr = re.sub("(bag[s]*[\.]*)", "", b)
                c = rawBagStr.split(" ")[0]
                s = rawBagStr.replace(" ", "")
                bagRelName = re.sub(r'[\d]*', "", s)
                bagsRel.append(c + "#" + bagRelName)
        bags[bagName] = bagsRel

    maxBags = 0
    for ref in bags:
        if ref == "shinygold":
            c = buildBagTree(bags, ref, 0, bags[ref])
            if c > maxBags:
                maxBags = c

    print("B): ", maxBags)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
