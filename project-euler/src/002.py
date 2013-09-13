#!/usr/bin/python
fib1 = 1
fib2 = 2
s = 0
while fib2 < 4000000:
    if (fib2 % 2 == 0):
        s = s + fib2
    tmp = fib2
    fib2 = fib1 + fib2
    fib1 = tmp

print (s)
