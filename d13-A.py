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

def a():
    rows = [n for n in readInput().split('\n')]
    arivalTime = int(rows[0])
    busesTmp = rows[1].split(",")
    buses = []
    for bus in busesTmp:
        if bus != "x":
            buses.append(int(bus))

    minWaitTime = sys.maxsize
    waitTimes = []    
    for bus in buses: 
        depTime = 0
        while depTime < arivalTime:
            depTime += bus
        waitTime = depTime - arivalTime
        waitTimes.append(waitTime)

    minWaitTime = min(waitTimes)
    ind = waitTimes.index(minWaitTime)  
    firstBus = buses[ind]

    busId = minWaitTime * firstBus
    print("A): ", minWaitTime, busId, firstBus)
    print("A): ", busId)

class Bus:
    def __init__(self, busId, pos):
        self.id = busId
        self.pos = pos

    def p(self):
        print("Bus: {} at pos {}".format(self.id, self.pos))

def getStats(b, c):
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

def b():
    rows = [n for n in readInput().split('\n')]
    busesTmp = rows[1].split(",")
    buses = []

    start = 1
    for i in range(len(busesTmp)):
        bus = busesTmp[i]
        if bus != "x":
            b = Bus(int(bus), i)
            buses.append(b)
            
    maxStart = 0
    maxJump = 0
    for i in range(len(buses)):
        for j in range(len(buses)):
            stats = getStats(buses[i], buses[j])
            if stats[1] > maxJump:
                maxJump = stats[1]
                maxStart = stats[0]
    print(maxStart, maxJump)

    start = maxStart
    jump = maxJump
    t = start

    #print(tp)
    match = False
    firstBus = buses[0]
    lastBus = buses[len(buses)-1]
    while not match:

        fbdpt = t%firstBus.id == 0  
        lbdpt = (t+lastBus.pos)%lastBus.id == 0

        if t%100000000 == 0:
            print("HUNDRED Milly", t)
        
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
                print(t)
        t += jump   
    

# Main body
if __name__ == '__main__':
    start = time.time()
    a()
    b()

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
