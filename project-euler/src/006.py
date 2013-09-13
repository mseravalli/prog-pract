#!/usr/bin/python
import math

sumOfSquares = 0
squareOfSum = 0

for i in range (1, 101):
    sumOfSquares = sumOfSquares + (i*i)
    squareOfSum = squareOfSum + i

squareOfSum = squareOfSum * squareOfSum

print (abs(sumOfSquares - squareOfSum))

