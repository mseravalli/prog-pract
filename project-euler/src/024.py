#!/usr/bin/python

l = 9
max_iter = 1000000
digits = []
digits.extend(range(l+1))
swap = digits[::-1]

c = l

i = 0
while (True):
    i+=1
    while (c >= 0):
        if(swap[c] == 0):
            c -= 1
        else:
            break

    if (c == -1 or i>= max_iter):
        print i, digits
        break

    tmp = digits[c + swap[c]]
    digits[c + swap[c]] = digits[c]
    digits[c] = tmp
    swap[c] -= 1

    offset = c + 1
    while (c < l):
        c += 1
        swap[c] = l-c
        start = c
        end = l - (c - offset)
        if (start < end):
            tmp = digits[start]
            digits[start] = digits[end]
            digits[end] = tmp

