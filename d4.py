#!/user/bin/env python3 -tt
"""
Task:
https://adventofcode.com/2020/day/4
"""

# Imports
import sys
import os
import re
import math

# Global variables
task="d4"
infile=task + ".input"

def readInput():
    with open('input/' + infile) as file:
        data = file.read()
    file.close()
    return data

def validateFields(key, value):
    valid = False


    return valid

def validatePassportA(passport):
    expectedFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fieldKeys = []
    for f in passport:
        fieldKeys.append(f.split(":")[0])    
    fieldKeys.sort()

    for f in expectedFields:
        if f not in fieldKeys:
            return False
    return True      

def validatePassportB(passport):
    expectedFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fieldKeys = []
    for f in passport:
        key = f.split(":")[0]
        value = f.split(":")[1]
        if validateFields(key, value):
            fieldKeys.append(f.split(":")[0])
    
    fieldKeys.sort()

    #print("Validate fieldkeys: ", fieldKeys)
    for f in expectedFields:
        if f not in fieldKeys:
            return False
    return True 

def extractPassports(rows):
    passports = []
    pp = ""
    for row in rows:
        if len(row) < 3:
            passports.append(pp.split(" "))
            pp = "" 
        else:
            if len(pp) == 0:
                pp += row
            else:
                pp += " " + row
    print("Found passports: ", len(passports))
    return passports

def a():
    rows = [n for n in readInput().split('\n')]
    passports = []
    count = 0

    passports = extractPassports(rows)

    for passport in passports:
        if validatePassportA(passport):
            count += 1
        #print(passport, validatePassport(passport))

    print("A): ", count)

def b():
    rows = [n for n in readInput().split('\n')]
    passports = []
    count = 0

    passports = extractPassports(rows)

    for passport in passports:
        if validatePassportA(passport):
            count += 1
        #print(passport, validatePassport(passport))

    print("B): ", count)
# Main body
if __name__ == '__main__':
    a()
#    b()
    sys.exit(1)
