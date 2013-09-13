#!/usr/bin/python

ones = ["one","two","three","four",
        "five","six","seven","eight","nine"]
tens = ["ten","eleven","twelve","thirteen","fourteen",
        "fifteen","sixteen","seventeen","eighteen","nineteen"]
twenties = ["twenty","thirty","forty",
            "fifty","sixty","seventy","eighty","ninety"]

s = 0

for num in ones:
    s += len(num)
    print num

for num in tens:
    s += len(num)
    print num

for dec in twenties:
    s += len(dec)
    print(dec)
    for un in ones:
        s += len(dec+un)
        print(dec+un)

for hun in ones:
    s += len(hun + "hundred")
    print(hun + "hundred")
    for num in ones:
        s += len(hun + "hundredand" + num)
        print(hun + "hundredand" + num)

    for num in tens:
        s += len(hun + "hundredand" + num)
        print(hun + "hundredand" + num)

    for dec in twenties:
        s += len(hun + "hundredand" + dec)
        print(hun + "hundredand" + dec)
        for un in ones:
            s += len(hun + "hundredand" + dec+un)
            print(hun + "hundredand" + dec+un)

s += len("onethousand")

print(s)


test = ["one","two","three","four","five"]
s = 0
for num in test:
    s += len(num)
print s
