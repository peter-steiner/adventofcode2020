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
    #print("#################", x, y)
    
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
                    surrounding.append(snapshot[y1][x1])
                    #print(x, y, x+xp, y+yp, snapshot[x+xp][y+yp],snapshot[x1][y1])
                    surrounding.append("Z")
               
    #print("Sur: ",x, y, surrounding)
    if surrounding.count("X") >= 4:
        waitingroom[y][x] = "L"
    if surrounding.count("X") == 0:
        waitingroom[y][x] = "X"

    return 
#    if surrounding.count("X") < 4 and surrounding.count("X") > 0:
#        return 


def a():
    seats = [n for n in readInput().split('\n')]
    waitingRoom = []
    res = 0

    for s in seats: 
        waitingRoom.append(list(s))
    
    yMax = len(waitingRoom)
    xMax = len(waitingRoom[0])
    print("1", xMax, yMax)

#########################    
    equals = True
    it = 0
    while equals:
        snapshot = []
        for y in range(yMax):
            snapshot.append(waitingRoom[y][0:])

        print("2", len(snapshot[0]), len(snapshot))
#        for s in snapshot: 
#            print(s)
#        print("----------------------------------------------------")
        
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
#        print("#####################################################")

#########################    
   

    print("a):", res)

def b():
    ratings = [int(n) for n in readInput().split('\n')]
    result = 0
    print("B):", result)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)



"""
    # UP 
    try:
        u = snapshot[x][y+1]
    except:
        u = "Z"
    # UP RIGHT
    try:
        r = snapshot[x+1][y+1]
    except:
        ur = "Z"
    # RIGHT
    try:
        r = snapshot[x+1][y]
    except:
        r = "Z"
    # DOWN Right
    try:
        d = snapshot[x-1][y]
    except:
        d = "Z"
    # DOWN 
    try:
        d = snapshot[x-1][y]
    except:
        d = "Z"
    #LEFT
    try:
        l = snapshot[x][y-1]
    except:
        l = "Z"

    surrounding = [u, r, d, l]
    if surrounding.count("X") == 4:
        waitingroom[x][y] = "L"
    if surrounding.count("X") == 0:
        waitingroom[x][y] = "X"
"""
