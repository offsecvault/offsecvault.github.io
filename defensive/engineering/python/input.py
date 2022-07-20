#!/bin/python3

import sys

# === S T R I N G ===

# name = input("Type your name: ")
# print("My name is: " + name)


# === I N T E G E R ===

# x = int(input("Type number: "))
# y = int(input("Type second number: "))

# print(x + y)

# === F L O A T ===

# x = float(input("Number One: "))
# y = float(input("Number Two: "))

# print(x + y)


# === C A L C U L A T O R ===

x = float(input("Type number one: "))
o = input("Type an operator: ")
y = float(input("Type number two: "))

if o == "+":
    print(x + y)
elif o == "-":
    print(x - y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
else:
    print("Not valid option")





