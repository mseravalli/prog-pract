#!/usr/bin/python
import math

def gcd(x,y):
    if x%y == 0:
        return y
    else:
        return gcd(y,x%y)
            
def lcm(x,y):
    return abs(x*y)/gcd(x,y)

y = 1
x = 1
while x < 21:
        y = lcm(y,x)
        x =x + 1 
print y

# def isPrime(num):
#     fact = math.ceil(math.sqrt(num))
#     while(num % fact != 0):
#         fact = fact - 1
#     if (fact == num or fact == 1):
#         return True
#     return False
# 
# num = 1
# top = 20
# for i in range (top, 0, -1):
#     if (num % i != 0):
#         num = num * i
# 
# for i in range (top, 1, -1):
#     if (isPrime(i)):
#         canDivide = True
#         while canDivide:
#             attempt = num / i
#             for j in range (top, 0, -1):
#                 if (attempt % j != 0):
#                     canDivide = False
#             if (canDivide):
#                 num = num / i
# 
# print (num)
