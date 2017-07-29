state = 1
import linecache
def input():
    global state
    result = linecache.getline('stockfile_2.txt', state)
    state += 1
    return result

import numpy as np
m,kf,df = map(float,input().split())
k = int(kf)
stckop = {}
for i in range(k):
    row = list(input().split())
    stockname, stocks, history = row[0], int(row[1]),list(map(float,row[2:]))
    #print(history)
    x = np.arange(0,len(history))
    y = np.array(history)
   # import matplotlib.pyplot as plt
   # plt.plot(x,y)
    pf = np.polyfit(np.arange(0,len(history)),np.array(history),1)
    ev1 = pf[0]*len(history)  + pf[1]
    ev2 = pf[0]*(len(history)-1) + pf[1]
    exv = ev1 - ev2 + history[-1]
 #   print(stockname, history[-1], exv)

    stckop[stockname] = {"n" : stocks, "y" : history[-1], "t" : exv}
#print(stckop)
#plt.show()
bestbuys = sorted([x for x in stckop.items() if x[1]["t"] > x[1]["y"]], key=lambda x: x[1]["t"] - x[1]["y"],reverse=True)
shouldsell = sorted([x for x in stckop.items() if x[1]["n"] > 0 and x[1]["t"] < x[1]["y"]], key=lambda x: x[1]["t"] - x[1]["y"])
#print(bestbuys)
#print(shouldsell)
trns = []
for ss in shouldsell:
    trns.append((ss[0],"SELL",int(ss[1]["n"])))
#    print("{} SELL {}".format(ss[0],int(ss[1]["n"])))
for bb in bestbuys:
    if (m > 0):
        tb = m // bb[1]["t"]
#        trns.append({"s": bb[0], "a": "BUY", "q": int(tb)})
        if (tb > 0):
            trns.append((bb[0], "BUY", int(tb)))
        #
#        print("{} BUY {}".format(bb[0],int(tb)))
        m = m - tb*bb[1]["t"]

print(len(trns))
for trn in trns:
    print(*trn)
