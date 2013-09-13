#!/usr/bin/python

reg  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

curr = 2
sundays = 0

for year in range(1901, 2001):
    if ((year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0):
        month = leap
    else:
        month = reg

    for m in month:
        curr += m
        if (curr % 7 == 0):
            sundays += 1

print sundays

# import datetime
# count = 0
# for y in range(1901,2001):
#     for m in range(1,13):
#         if datetime.datetime(y,m,1).weekday() == 6:
#            count += 1
# print count
