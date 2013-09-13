#!/usr/bin/python

lim = 1000
a = [0]*lim
b = [0]*lim
res = [0]*lim

a[0] = 1
b[0] = 1

count = 2

carry = 0
isFound = False
while (not isFound):
    count +=1
    for i in range(0, lim):
        tmp = a[i] + b[i] + carry
        res[i] = tmp % 10
        if(tmp > 0):
            carry = int(tmp / 10)
        else:
            carry = 0
        if(i == lim - 2 and carry > 0):
            isFound = True

    for i in range(0, lim):
        a[i] = b[i]
        b[i] = res[i]

print count

