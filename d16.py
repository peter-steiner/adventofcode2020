#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/16
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d16"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def a():
    rows = [n for n in readInput().split('\n')]
    
    itRow = 0
    rowCount= len(rows)
    numbers = ["X"]*1000
    # Rules
    print("-------------")
    for i in range(rowCount):
        row = rows[i]
        ranges = re.findall(r"(\d+-\d+)",row)
        for rng in ranges:
            frm, to = rng.split("-")
            for n in range(int(frm), int(to)+1):
                numbers[n] = "C"
    
        itRow += 1
        if len(row) == 0:    
            break

    print("-------------")
    for i in range(itRow, rowCount):
        row = rows[i]
        print(row)
        itRow += 1
        if len(row) == 0:    
            break

    sum = 0
    print("-------------")
    ticketsCount = 0
    for i in range(itRow+1, rowCount):
        row = rows[i]
        print(row)
        valid = True
        ticketValues = row.split(",")
        for tkv in ticketValues:
            if numbers[int(tkv)] == "X":
                sum += int(tkv) 
                print("Invalid ticket", tkv, ticketValues)
                valid = False

        if valid: 
            ticketsCount += 1

    print("COntinue", ticketsCount)
    print("A): ", sum)

def b():
    rows = [n for n in readInput().split('\n')]

    print("B): ")

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
