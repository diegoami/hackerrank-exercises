import numpy as np

state = 0
inputarray = [ "1.50" ]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result


#!/bin/python3

import sys
import numpy as np
tdn = np.loadtxt('trainingdata.txt',delimiter=',')
#import matplotlib.pyplot as plt
#plt.scatter(tdn[:,0], tdn[:,1])
#plt.show()
#print(tdn)
#cofav = tdn[:,1]/tdn[:,0]
#print(cofav)

#pf = np.polyfit(tdn[:,0], tdn[:,1],1)
#print(pf)

timeCharged = float(input().strip())
#timeExpected = pf[0]*timeCharged + pf[1]
#print(timeExpected)
if (timeCharged >= 4):
    print(8)
else:
    print(timeCharged*2)
