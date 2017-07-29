state = 1
import linecache
def input():
    global state
    result = linecache.getline('stockfile_1.txt', state)
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
    #x = np.arange(0,len(history)+1)
    x = np.arange(0,4)
    #x = np.logspace(2, 3, num=len(history)+1)
    y = np.array(history[-3:])
    #import matplotlib.pyplot as plt
    #plt.plot(x[:-1],y)
    pf = np.polyfit(x[:-1],y,1)
    ev1 = pf[0]*x[-2]  + pf[1]
    ev2 = pf[0]*x[-1] + pf[1]
    exv = ev2 - ev1 + history[-1]
    print(stockname, history[-1], exv)
    print(x,y)
    stckop[stockname] = {"n" : stocks, "y" : history[-1], "t" : ev2}
#print(stckop)
#plt.show()
bestbuys = sorted([x for x in stckop.items() if x[1]["t"] > x[1]["y"]], key=lambda x: x[1]["t"] - x[1]["y"],reverse=True)
shouldsell = sorted([x for x in stckop.items() if x[1]["n"] > 0 and x[1]["t"] < x[1]["y"]], key=lambda x: x[1]["t"] - x[1]["y"])
#print(bestbuys)
#print(shouldsell)
trns = []
for ss in shouldsell:
    trns.append((ss[0],"SELL",max(int(ss[1]["n"]) // 2 ,1)))
    #trns.append((ss[0],"SELL",int(ss[1]["n"])))
#    print("{} SELL {}".format(ss[0],int(ss[1]["n"])))
for bb in bestbuys:
    if (m > 0):
        tb = m // bb[1]["y"]
#        trns.append({"s": bb[0], "a": "BUY", "q": int(tb)})
        if (tb > 0):
            trns.append((bb[0], "BUY", int(tb)))
        #
#        print("{} BUY {}".format(bb[0],int(tb)))
        m = m - tb*bb[1]["y"]

print(len(trns))
for trn in trns:
    print(*trn)
