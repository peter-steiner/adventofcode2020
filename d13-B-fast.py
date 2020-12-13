#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/13
"""

# Imports
import sys
import os
import re
import math
import time
# Global variables
task="d13"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

class Bus:
    def __init__(self, busId, pos):
        self.id = busId
        self.pos = pos

    def p(self):
        print("Bus: {} at pos {}".format(self.id, self.pos))

def getCommonUnion(b, c):
    n = 0
    p = 0
    prev = 0
    diff = []
    while p < 3:
        if (n+b.pos)%b.id == 0 and (n+c.pos)%c.id == 0:
            diff.append(abs(prev-n))
            prev = n
            p += 1
        n +=1
    return diff

def getNextCommonUnion(bus, jump, start):
    n = start
    p = 0
    prev = 0
    diff = []
    while p < 3:
        if (n+bus.pos)%bus.id == 0:
            diff.append(abs(prev-n))
            prev = n
            p += 1
        n += jump
    return diff

def b():
    rows = [n for n in readInput().split('\n')]
    busesTmp = rows[1].split(",")
    buses = []

    for i in range(len(busesTmp)):
        bus = busesTmp[i]
        if bus != "x":
            b = Bus(int(bus), i)
            buses.append(b)
    maxStart = 0
    maxJump = 0
    handled = []
    for i in range(len(buses)):
        for j in range(len(buses)):
            if i != j:
                stats = getCommonUnion(buses[i], buses[j])
                if stats[1] > maxJump:
                    handled.append(j)
                    maxJump = stats[1]
                    maxStart = stats[0]
    #print(maxStart, maxJump)
    for i in range(len(buses)):
        if i not in handled:
            #print("Run", i, buses[i].id)
            stats = getNextCommonUnion(buses[i], maxJump, maxStart)
            handled.append(i)
            maxStart = stats[0]
            maxJump = stats[1]
            #print(stats)
    jump = maxJump
    t = maxStart

    print("Start at: {} and jump {}".format(t, jump))
    match = False
    firstBus = buses[0]
    lastBus = buses[len(buses)-1]
    while not match:
        fbdpt = t%firstBus.id == 0  
        lbdpt = (t+lastBus.pos)%lastBus.id == 0        
        # possible match
        if fbdpt and lbdpt:
            count = 0
            for b in range(1, len(buses)):
                bus = buses[b]
                # Match, continue
                if (t+bus.pos)%bus.id == 0:
                    count += 1
            if count == len(buses)-1:
                match = True
                print("Found a match: ", t)

        t += jump   
    

# Main body
if __name__ == '__main__':
    start = time.time()
    b()

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
