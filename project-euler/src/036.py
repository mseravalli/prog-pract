#!/usr/bin/python

print sum(i for i in xrange(1000000) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1] )

