#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/22
"""

# Imports
import sys
import os
import re
import math
import time

# Global variables
task="d22"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data
gameG = 0
def recursiveCombat(p1, p2):
    global gameG
    gameG += 1
    game = gameG
    #print("Enter Game {} with \n{}\n{}".format(game, p1[::-1], p2[::-1]))
    stack = []
    winnerStack = []
    #for i in range(1, 10):
    p1Hands = []
    p2Hands = []
    i = 0
    while True:
        i += 1
        """
        print("-- Round " , i, " (Game", game, ") --")
        print("Player 1's deck: {} \nPlayer 2's deck: {}".format(p1, p2))
        print("Player 1 plays: ", p1[-1])
        print("Player 2 plays: ", p2[-1])
        """
        # Check each players hand with previous hands
        p2tmp = ",".join([str(n) for n in p2])
        p1tmp = ",".join([str(n) for n in p1])
        if p1tmp in p1Hands or p2tmp in p2Hands:
            """
            print("Player 1 wins round", i, "out of game ", game, "!")
            print("Winner: P1", p1tmp, p2tmp, p1Hands)
            """
            winnerStack = p1[:]
            return [False, "p1", winnerStack]
        # Add dealing to history
        p1Hands.append(p1tmp) 
        p2Hands.append(p2tmp) 

        """
        if p2tmp in p2Hands:
            print("Player 2 wins round", i, "out of game ", game, "!")
            print("Winner: P2", p2, p2Hands)
            winnerStack = p2[:]
            return [False, "p2", winnerStack]
        """
        # Play hands
        c1 = p1.pop()
        c2 = p2.pop()
        stack.append(c1) 
        stack.append(c2) 

        # C1 as default winner
        winner = ""
        # Subgame of recursive combat
        #print("Seriöst P1", c1, p1, len(p1), c1 >= len(p1))
        #print("Seriöst P2", c2, p2, len(p2), c2 >= len(p2))
        if c1 <= len(p1) and c2 <= len(p2):
            #print("-- Round " , i, "-- ENTER RECURSIVE HELL --- GAME ", game)
            #print("Playing a sub-game to determine the winner...")
            break_, winner, winnerStack = recursiveCombat(p1[len(p1)-c1:], p2[len(p2)-c2:])
            
            if break_:
                print("###################\n####################\n##############")
                return [False, winner, winnerStack]

        if winner == "":    
            # C2 wins
            ls = len(stack)
            if stack[ls-2] < stack[ls-1]:
                winner = "p2"
            else:
                winner = "p1"

        #print("winner", winner, stack)
        while len(stack) > 0:
            if winner == "p2":  
                p2.insert(0, stack.pop())
                p2.insert(0, stack.pop())
            else:
                p1.insert(0, stack.pop(0))
                p1.insert(0, stack.pop(0))
        #print("p1, p2\n-- Round ", i, " --\n", p1[::-1], p2[::-1])
        if not p1:
            #print("Player 2 wins round", i, "out of game ", game, "!")
            winnerStack = p2[:]
            winner = "p2"
            return [False, winner, winnerStack]
        if not p2:
            #print("Player 1 wins round", i, "out of game ", game, "!")
            winner = "p1"
            winnerStack = p1[:]
            return [False, winner, winnerStack]
    return [False, winner, winnerStack]

def a():
    rows = [n for n in readInput().split('\n')]

    p1 = []
    p2 = []
    
    p = []
    for row in rows:
        if "Player" in row:
            print("Reading p1")
        else:
            if len(row) == 0:
                p1 = p[:]
                p = []
            else:
                p.append(int(row))
    p2 = p[:]
    # Reverse and place deck on table
    p1 = p1[::-1]
    p2 = p2[::-1]

    print("Starting hands Player 1", p1)
    print("Starting hands Player 2", p2)

    break_, winner, winnerStack = recursiveCombat(p1, p2)
    if break_:
        print("Hard break")

    points = 0
    for i in range(len(winnerStack)):
        print(i+1, winnerStack[i], (i+1)*winnerStack[i])
        points += (i+1)*winnerStack[i]  
    res = 0
    print("B): ", points)

# Main body
if __name__ == '__main__':
    start = time.time()

    a()
    end = time.time()
    exectime = end - start
    print("Executed A in: {}".format(exectime))

    end = time.time()
    exectime = end - start
    print("Executed in: {}".format(exectime))
    sys.exit(1)
