#!/usr/bin/python

fo = open("015.txt", "r") 
lines = fo.readlines()
fo.close()

print (str(sum([int(x) for x in lines]))[:10])
#res = 0
#for l in lines:
#    res += int(l)
#
#print (res)
