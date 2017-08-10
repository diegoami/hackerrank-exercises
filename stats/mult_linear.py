
inputarray = [
"2 7",
"0.18 0.89 109.85",
"1.0 0.26 155.72",
"0.92 0.11 137.66",
"0.07 0.37 76.17",
"0.85 0.16 139.75",
"0.99 0.41 162.6",
"0.87 0.47 151.77",
"4",
"0.49 0.18",
"0.57 0.83",
"0.56 0.64",
"0.76 0.18"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)
import numpy as np
X,Y,XV = None, None, None

m,k = map(int,input().split())
for i in range(k):
    lt = list(map(float,input().split()))
    xt = [1]+lt[:-1]
    yt = [lt[-1]]
    X = np.array(xt) if X is None else np.vstack((X, xt))
    Y = np.array(yt) if Y is None else np.vstack((Y, yt))
n = int(input())
for i in range(n):
    xv = [1]+list(map(float,input().split()))
    XV = np.array(xv) if XV is None else np.vstack((XV,xv))

xtx = np.dot(X.T,X)
#print(xtx)
xtxi = np.linalg.inv(xtx)
xtxixt= np.dot(xtxi,X.T)
#print(xtxixt)
B = np.dot(xtxixt,Y)
#print(B)
R = np.dot(XV,B)
rl = R.tolist()
for rw in rl:
    for r in rw:
        rf = float(r)
        print("{:.2f}".format(rf))
