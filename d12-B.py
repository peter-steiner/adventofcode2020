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
def moveShip(instruction, x, y, sx, sy):
    comp = re.compile("([a-zA-Z]+)([0-9]+)") 
    action, value = comp.match(instruction).groups() 
    value = int(value)
    
    if action == "R":
        if value >= 180:
            x = -x
            y = -y
            #Handle 270 (290-180 = 90)
            value -= 180
        if value == 90:
            # [1, -1]
            nv = [y, -x]
            x = nv[0]
            y = nv[1]

    if action == "L":
        if value >= 180:
            x = -x
            y = -y
            #Handle 270 (290-180 = 90)
            value -= 180
        if value == 90:
            # [1, -1]
            nv = [-y, x]
            x = nv[0]
            y = nv[1]

    if action == "E":
        x += value
    if action == "W":
        x -= value
    if action == "S":
        y -= value
    if action == "N":
        y += value

    if action == "F":
        sx += value * x
        sy += value * y 

    return x, y, sx, sy

def a():
    instructions = [n for n in readInput().split('\n')]
    x = 10
    y = 1
    sx = 0
    sy = 0

    for instr in instructions:
        x, y, sx, sy = moveShip(instr, x, y, sx, sy)
        #print("-------------------------------")

    print("A): ", abs(sx)+abs(sy))

# Main body
if __name__ == '__main__':
    a()
    sys.exit(1)
