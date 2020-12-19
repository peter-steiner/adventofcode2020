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

def cleanRows(rows):
    itRow = 0
    rowCount= len(rows)
    numbers = ["X"]*1000
    rules = []
    myTicket = []
    nearbyTickets = []
    # Rules
    for i in range(rowCount):
        row = rows[i]
        if len(row) == 0:    
            itRow += 1
            break
        rules.append(row)
        ranges = re.findall(r"(\d+-\d+)",row)
        for rng in ranges:
            frm, to = rng.split("-")
            for n in range(int(frm), int(to)+1):
                numbers[n] = "C"
        itRow += 1

    for i in range(itRow, rowCount):
        row = rows[i]
        itRow += 1
        if bool(re.search(r'\d', row)):
            myTicket = row
        if len(row) == 0:    
            break
    sum = 0

    for i in range(itRow+1, rowCount):
        row = rows[i]
        valid = True
        ticketValues = row.split(",")
        for tkv in ticketValues:
            if numbers[int(tkv)] == "X":
                sum += int(tkv) 
                valid = False
        if valid:
            nearbyTickets.append(row)
        if len(row) == 0:    
            break
    return [rules, myTicket, nearbyTickets]


def b():
    rows = [n for n in readInput().split('\n')]
    rulesRaw = []
    myTicketRaw = []
    nearbyTicketsRaw = []

    rulesRaw, myTicketRaw, nearbyTicketsRaw = rows = cleanRows(rows)
    rules = []
    ruleNames = []

    # Rules
    print("-------------")
    for i in range(len(rulesRaw)):
        row = rulesRaw[i]
#        print("Rule", row)
        ruleName = "".join(row.split(":")[0].split(" "))
        ruleNames.append(ruleName)
        ranges = re.findall(r"(\d+-\d+)",row)
        numbers = []
        for rng in ranges:
            frm, to = rng.split("-")
            numbers.append(int(frm))
            numbers.append(int(to))
        rules.append(numbers)        
        
    tickets = []
    print("Nearby Tickets-------------", len(nearbyTicketsRaw))
    for nbtr in nearbyTicketsRaw:
        ticketValues = [int(i) for i in nbtr.split(",")]
        tickets.append(ticketValues)

    ticketLength = len(tickets[0])
    # init valid rules
    validRules = []
    for i in range(ticketLength):
        validRules.append([])

    for d in range(ticketLength):
        ticketsVal = []
        for t in tickets:
            val = t[d]
            ticketsVal.append(val)

        vl = len(tickets)
        for i in range(len(rules)):
            validRulesCount = 0
            for val in ticketsVal:
                if rules[i][0] <= val <= rules[i][1] or rules[i][2] <= val <= rules[i][3]:
                    validRulesCount += 1
            if validRulesCount == vl:
                b = validRules[d]
                b.append(ruleNames[i])

    # attempts
    deteminedRules = ["X"]*ticketLength
    for i in range(11):
        for i in range(ticketLength):
            if len(validRules[i]) == 1:
                name = validRules[i][0]
                deteminedRules[i] = name
                for rules in validRules:
                    if name in rules:
                        rules.remove(name)
 
    print("Determined rules", deteminedRules)
    myTicketValues = [int(n) for n in myTicketRaw.split(",")]
    product = 1
    for dr in deteminedRules:
        if "departure" in dr:
            ind = deteminedRules.index(dr)
            product *= myTicketValues[ind]

    print("B): ", product)

# Main body
if __name__ == '__main__':
    start = time.time()

    b()
    end = time.time()
    exectime = end - start
    print("Executed B in: {}".format(exectime))
