
inputarray = [
    "20 2",
    "19.5",
    "20 22"
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
min_b = float(input())
bet_1, bet_2 = map(float,input().split())

z_min_b = (min_b-mu)/si
z_bet_1, z_bet_2 = (bet_1-mu)/si , (bet_2-mu)/si


p_l = phi(z_min_b)
p_b = phi(z_bet_2) - phi(z_bet_1)

print(round(p_l,3))
print(round(p_b,3))

