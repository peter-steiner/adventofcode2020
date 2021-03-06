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

# Global  variables
task="d7"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def buildBagTree(bags, name, references, path, it):
    it += 1
    # is empty
    if len(references) == 0:
        return name
    if "shinygold" in references:
        return "shinygold"
    #visit children if not already visited
    for bagName in references:
        if bagName not in path:
            path += " " + buildBagTree(bags, bagName, bags[bagName], path, it)
            path = " ".join(set(path.split(" ")))
    return path

def a():
    rows = [n for n in readInput().split('\n')]
    res = 0

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
                s = re.sub("(bag[s]*[\.]*)", "", b).replace(" ", "")
                bagRelName = re.sub(r'[\d]*', "", s)
                bagsRel.append(bagRelName)
        bags[bagName] = bagsRel

    for ref in bags:
        rawPath = buildBagTree(bags, ref, bags[ref], "", 0)
        tree = " ".join(set(rawPath.split(" ")))
        if "shinygold" in tree:
            res += 1

    print("A): ", res)


# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
