#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/11
"""

# Imports
import sys
import os
import re
import math
import itertools

# Global variables
task="d11"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def checkSeat(snapshot, waitingroom, y, x): 
    
    if snapshot[y][x] == ".":
        return 

    yMax = len(snapshot)
    xMax = len(snapshot[0])

    dirs = [-1, 0 , 1]
    surrounding = []
    for xp in dirs:
        for yp in dirs: 
            x1 = x+xp
            y1 = y+yp
            if x != x1 or y != y1:
                if x1 >= 0 and x1 < xMax and y1 >= 0 and y1 < yMax:
                    x1 = x+xp
                    y1 = y+yp
                    direction = snapshot[y1][x1]
                    if direction == "L" or direction == "X":
                        surrounding.append(direction)
                    if direction == ".": 
                        # Try further in path
                        for n in range(2,xMax):
                            x2 = x+n*xp
                            y2 = y+n*yp        
                            if x2 >= 0 and x2 < xMax and y2 >= 0 and y2 < yMax:
                                direction = snapshot[y2][x2]
                                if direction == "L" or direction == "X":
                                    surrounding.append(direction)
                                    break
    if surrounding.count("X") >= 5:
        waitingroom[y][x] = "L"
    if surrounding.count("X") == 0:
        waitingroom[y][x] = "X"

    return 


def a():
    seats = [n for n in readInput().split('\n')]
    waitingRoom = []
    res = 0

    for s in seats: 
        waitingRoom.append(list(s))
    
    yMax = len(waitingRoom)
    xMax = len(waitingRoom[0])

#########################    
    equals = True
    it = 0

#    for i in range(3):
    while equals:
        snapshot = []
        for y in range(yMax):
            snapshot.append(waitingRoom[y][0:])

        #for s in snapshot: 
        #    print(s)
        #print("----------------------------------------------------")
        
        for y in range(yMax):
            for x in range(xMax):
                checkSeat(snapshot, waitingRoom, y, x)

        for y in range(yMax):
            for x in range(xMax):
                if snapshot[y][x] != waitingRoom[y][x]:
                    equals = False
        sum = 0
        if equals:
            for y in range(yMax):
                sum += waitingRoom[y].count("X")
            print("Stabilized chaoz in iterations {} and buzy seats: {}".format(it, sum))
            break
        it += 1
        equals = True   

    print("a):", res)

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)