#!/bin/python3

def readFile():
    filepath = "/home/scripting/sites.csv"
    file = open(filepath, 'r')
    count = 0
    
    while True:
        count += 1
        site = file.readline()
        if not site:
            break
        print(site.strip())

readFile()

