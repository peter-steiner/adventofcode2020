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


    

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
