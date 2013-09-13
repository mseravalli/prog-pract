#!/usr/bin/python
import math

def isPalindrome(num):
    string = str(num)
    length = len(string)
    for i in range(0, length/2 + 1):
        if (string[i] != string[length-1-i]):
            return False
    return True

solutions = []
for a in range(999, 9, -1):
    for b in range(999, 9, -1):
        mult = a*b
        if (isPalindrome(mult)):
            solutions.append(mult)

final = solutions[0]
for sol in solutions:
    if (final < sol):
        final = sol

print final
