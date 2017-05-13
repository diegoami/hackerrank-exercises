state = 0
inputarray = [
"95 85",
"85 95",
"80 70",
"70 65",
"60 70",
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import math
def mean(l):
    return sum(l)/len(l)


def stddev(l,mu):
    return math.sqrt(sum([(x-mu)**2 for x in l])/(len(l)))

def ro(xl,yl,mux,muy,stdx,stdy,n):
    return sum([(xl[i]-mux)*(yl[i]-muy) for i in range(len(xl))])/(n*stdx*stdy)

import sys
xl, yl = [], []
for i in range(5):
    x,y = map(int,input().split())
    xl.append(x)
    yl.append(y)

mux, muy  = mean(xl), mean(yl)
stdx, stdy = stddev(xl,mux), stddev(yl,muy)
roxy = ro(xl,yl,mux,mux, stdx,stdy,5)
b= roxy*stdy/stdx
a= muy - b * mux
res = b*80+a
#print(a,b)
#print(a,b)
print("{0:.3f}".format(res))
