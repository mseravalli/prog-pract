#!/usr/bin/python

fo = open("008.txt", "r") 
lines = fo.readlines()
fo.close()
string = ""
for l in lines:
    string = string + l

string = string.replace("\n", "")

res = 0

for i in range(0, len(string) - 5):
    tmp = 1
    for j in range(0, 5):
        tmp = tmp * int(string[i+j])
        if (tmp > res):
            res = tmp

print (res)
