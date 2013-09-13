#!/usr/bin/python

lim = 1000000
nums = [0]*lim
nums[1] = 1

for i in range(2, lim):
    currPos = i 
    steps = 1
    while (currPos != 1):
        if (currPos%2 == 0):
            currPos /= 2
        else:
            currPos = 3 *currPos + 1

        if (currPos < lim and nums[currPos] > 0):
            steps += nums[currPos]
            nums[i] = steps
            break
        else:
            steps += 1

m = 0
idx = 0
for i in xrange(len(nums)):
    if(nums[i]>m):
        idx = i
        m = nums[i]

print(idx)
