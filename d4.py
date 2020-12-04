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
    RE_INT = re.compile(r'^[0-9]+$')
    if key == "byr" and RE_INT.match(value):
        v = int(value)
        if v >= 1920 and v <= 2002: 
            return True
    if key == "iyr" and RE_INT.match(value):
        v = int(value)
        if v >= 2010 and v <= 2020: 
            return True
    if key == "eyr" and RE_INT.match(value):
        v = int(value)
        if v >= 2020 and v <= 2030: 
            return True
    if key == "hgt" and re.match(r'^([\d]+(cm|in))$', value):
        height = int(re.findall('[\d]+', value)[0])
        metric = value.replace(str(height), "")
        if metric == "cm":
            if height >= 150 and height <= 193: 
                return True
        if metric == "in": 
            if height >= 59 and height <= 76: 
                return True
    if key == "hcl" and re.match(r'^(#{1}([0-9|a-f]{6}))$', value):
        return True
    if key == "ecl" and re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', value):
#        print("valid haircolor: ", value)
        return True
    if key == "pid" and re.match(r'^([0-9]{9})$', value):
        return True
        
    return False

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
            fieldKeys.append(key)
    
    fieldKeys.sort()
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
    #print("Found passports: ", len(passports))
    return passports

def a():
    rows = [n for n in readInput().split('\n')]
    passports = []
    count = 0

    passports = extractPassports(rows)

    for passport in passports:
        if validatePassportA(passport):
            count += 1

    print("A): ", count)

def b():
    rows = [n for n in readInput().split('\n')]
    passports = []
    count = 0

    passports = extractPassports(rows)

    for passport in passports:
        if validatePassportB(passport):
            count += 1

    print("B): ", count)
# Main body
if __name__ == '__main__':
    a()
    b()
    sys.exit(1)
