#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/12
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d12"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

degrees = 0
def moveShip(instruction, x, y, degrees):
    comp = re.compile("([a-zA-Z]+)([0-9]+)") 
    action, value = comp.match(instruction).groups() 
    value = int(value)
    #print("B", action, value, x, y, degrees)
    
    prevD = degrees
    if action == "R":
        degrees += value
        if degrees >= 360:
            degrees = degrees - 360
        print("-------------------------------")
        print("TR: {} \tB {} \tA {}".format(instruction, prevD, degrees))

    if action == "L":
        degrees -= value
        if degrees < 0:
            degrees = 360 - abs(degrees)
        print("-------------------------------")
        print("TL: {} \tB {} \tA {}".format(instruction, prevD, degrees))
    
    if action == "E":
        x += value
    if action == "W":
        x -= value
    if action == "S":
        y += value
    if action == "N":
        y -= value
#--
    if degrees%180 == 0:
        if action == "F":
            if  degrees == 0:
                x += value
            else: 
                x -= value
                degrees = 180    
    # |
    # |        
    else:         
        if action == "F":
            if  degrees == 270:
                y -= value
            else: 
                y += value
        
    return x, y, degrees

def a():
    instructions = [n for n in readInput().split('\n')]
    x = 0
    y = 0
    degrees = 0
    """
    for instr in instructions:
        print(instr)
        x, y, degrees = moveShip(instr, x, y, degrees)
    """
    for i in range(0, len(instructions)):
        #print(instructions[i])
        x, y, degrees = moveShip(instructions[i], x, y, degrees)
        #print("-------------------------------")

    print("A): ", abs(x)+abs(y))

def b():
    rows = [int(n) for n in readInput().split('\n')]
    res = 0

    print("B): ", res)

# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
