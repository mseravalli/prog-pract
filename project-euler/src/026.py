#!/usr/bin/python

lim = 1000

length = [0]*lim
for d in range(2, lim):
    m = 0
    num = 1
    r = num
    isFound=False
    res = []

    while(not isFound):

        while(r > 0):
            m += 1
            r = num - m*d

        if(r==0):
            break

        r += d
        res.append(r)

        curr = len(res) - 1
        rec = res[curr]

        while(curr>0):
            curr -= 1
            if(res[curr] == rec):
                length[d] = len(res) - 1 - curr
                isFound=True
                break

        r *= 10
        num = r
        m=0


max_len = 0
idx = 0
for i in range(2, lim):
    if(length[i] > max_len):
        idx = i
        max_len = length[i]
print idx, max_len





