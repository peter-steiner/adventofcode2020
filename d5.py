#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/5
"""

# Imports
import sys
import os
import re
import math

# Global variables
#task="d5-t"
task="d5"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data


def findSection(cmd, section):
    l, u = section[0], section[1]
    h = round((u-l)/2)
    if h == 0:
        h=1
    if cmd == "F":
        # lower half
        u = u-h
    else:
        # Upper half
        l = l+h
    return [l, u]

def findSeat(cmd, seat):
    l, u = seat[0], seat[1]
    h = round((u-l)/2)
    if h == 0:
        h=1
    if cmd == "L":
        # lower half
        u = u-h
    else:
        # Upper half
        l = l+h
    return [l, u]

def a():
    bps = [n for n in readInput().split('\n')]
    
    sm = []
    cm = []
    seatIDs = []
    for bp in bps:
        section = [0, 127]
        seat = [0,7]
        
        sm = [n for n in bp[0:7]]
        cm = [n for n in bp[7:10]]
        
        for s in sm:
            section = findSection(s, section)
        for c in cm:
            seat = findSeat(c, seat)
        r, s = section[0], seat[0]
        seatID = r*8+s
        seatIDs.append(seatID)

    seatIDs.sort()
#    print(seatIDs)
    maxSeatID = max(seatIDs)
    print("A): ", maxSeatID)
    
    for n in range(1, len(seatIDs)-1):
        t = seatIDs[n]
        if seatIDs[n-1] != (t-1) or seatIDs[n+1] != (t+1):
            print("B) My seat:", seatIDs[n] + 1)
            break

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
