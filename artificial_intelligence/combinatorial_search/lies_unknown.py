
inputArray = [
"20 1 2 2 0",
"2",
"2 1 NO",
"3 4 NO"
]
from tools import input, initArrayInputter
initArrayInputter(inputArray)
from itertools import product

def gcmb(D, K):

     cart = product(range(K),repeat=D)
     return cart

N, pl_flag, L, K, L_max = map(int,input().split())
D = int(input())
conds = []

for i in range(D):
    As,Bs,resp = input().split()
    A,B = int(As)-1, int(Bs)-1
    conds.append({"A":A, "B":B, "R":1 if resp == 'YES' else 0 })


pd = gcmb(N,K)
allowedCombs = []
for p in pd:
    allowed = True
    for cond in conds:
         Ac = cond['A']
         Bc = cond['B']
         Rp = cond['R']
         if (p[Ac] == p[Bc] and not Rp) or (p[Ac] != p[Bc] and Rp):
             allowed = False
             print('Condition not fulfilled : ',cond)


    if allowed:
        allowedCombs.append(p)
        print('Accepting ',p)
    else:
        print('Rejecting ',p)


