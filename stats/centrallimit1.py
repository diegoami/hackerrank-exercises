state = 0
inputarray = [
   "9800",
    "49",
    "205",
    "15"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import math
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


weight    = float(input())
nboxes    = float(input())
weightbox = float(input())
stddev    = float(input())


mean_tot =  weightbox * nboxes
sig_tot = stddev * math.sqrt(nboxes)
#print(mean_tot, sig_tot)
z = (weight - mean_tot ) / sig_tot
#print(z)
print(round(phi(z),4))