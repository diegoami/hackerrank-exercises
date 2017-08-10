
inputarray = [
   "250",
"100",
"2.4",
"2.0"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import math
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


ntickets    = float(input())
nstudents   = float(input())
mean_p = float(input())
stddev_p    = float(input())


mean_tot =  mean_p * nstudents
sig_tot = stddev_p * math.sqrt(nstudents)
#print(mean_tot, sig_tot)
z = (ntickets  - mean_tot ) / sig_tot
#print(z)
print(round(phi(z),4))