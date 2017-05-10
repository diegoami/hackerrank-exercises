state = 0
inputarray = [
    "100",
    "500",
    "80",
    ".95",
    "1.96"
]

def input():
    global state
    result = inputarray[state]
    state += 1
    return result

import math
def phi(x):
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0


n    = float(input())
mu   = float(input())
si = float(input())
dist   = float(input())
z = float(input())

mean_tot =  mu * n
#print(mean_tot, sig_tot)
si_s = si / math.sqrt(n)
val1 = mean_tot - z*si_s
val2 = mean_tot + z*si_s
#print(z)
print(round(val1,2))
print(round(val2,2))