
inputarray = [
    "10",
    "10 9.8 8 7.8 7.7 7 6 5 4 2",
    "200 44 32 24 22 17 15 12 8 4"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import math


def mean(l):
    return sum(l)/len(l)


def stddev(l,mu):
    return math.sqrt(sum([(x-mu)**2 for x in l])/(len(l)))

def ro(xl,yl,mux,muy,stdx,stdy,n):
    return sum([(xl[i]-mux)*(yl[i]-muy) for i in range(len(xl))])/(n*stdx*stdy)

n    = float(input())
xl = list(map(float,input().split()))
yl = list(map(float,input().split()))

mux, muy = mean(xl), mean(yl)
stdx, stdy = stddev(xl,mux), stddev(yl, muy)
r = ro(xl,yl,mux,muy,stdx,stdy,n)
print(round(r,3))