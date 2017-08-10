
inputarray = [
   "70 10",
    "80",
    "60"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import sys
import math

import statistics as s
def gauss(x,mu, si):
    return math.exp(-(x-mu)**2/2*si**2)/(si*math.sqrt(2*math.pi))

def phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

mu, si = map(float,input().split())
hi_g = float(input())
pass_g = float(input())

z_hi_g = (hi_g-mu)/si
z_pass_g = (pass_g-mu)/si

print(round((1-phi(z_hi_g))*100,2))
print(round((1-phi(z_pass_g))*100,2))
print(round(phi(z_pass_g)*100,2))
