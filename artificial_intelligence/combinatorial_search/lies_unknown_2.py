
inputArray1 = [
"20 1 2 2 0",
"2",
"2 1 NO",
"3 4 NO"
]
inputArray2 = [
"10 1 1 2 0",
"5",
"1 2 NO",
"5 1 YES",
"9 0 YES",
"8 1 YES",
"0 9 NO",
]


inputArray3 = [
"10 1 1 2 0",
"10",
"8 0 YES",
"7 6 YES",
"4 5 NO",
"7 6 YES",
"6 8 NO",
"1 5 YES",
"1 7 NO",
"2 4 YES",
"5 2 YES",
"7 8 NO"
]

inputArray0 = [
"10 1 1 2 0",
"0"
]


inputArray5 = [
"10 1 1 2 0",
"13",
"0 9 YES",
"3 0 NO",
"2 8 YES",
"6 9 NO",
"6 5 NO",
"5 0 YES",
"4 8 NO",
"4 8 NO",
"5 8 NO",
"8 1 NO",
"2 9 YES",
"1 8 NO",
"7 2 YES"
]


inputArray6 = [
"10 1 1 2 0",
"11",
"8 7 NO",
"5 6 YES",
"1 4 NO",
"5 7 YES",
"4 5 NO",
"0 9 NO",
"4 9 YES",
"3 2 NO",
"7 2 YES",
"4 2 YES",
"2 7 NO"
]

inputArray7 = [
"10 1 1 2 0",
"13",
"6 3 NO",
"7 5 NO",
"3 4 YES",
"0 3 NO",
"1 7 YES",
"8 7 NO",
"0 1 NO",
"1 9 YES",
"2 6 NO",
"2 7 YES",
"9 4 YES",
"8 9 NO",
"7 5 NO"
]
inputArray8 = [
"30 1 2 3 0",
"21",
"28 12 NO",
"23 11 YES",
"5 6 YES",
"3 11 NO",
"15 22 NO",
"14 25 NO",
"16 19 NO",
"7 3 NO",
"19 2 NO",
"17 23 YES",
"9 19 NO",
"18 27 NO",
"10 4 NO",
"20 21 NO",
"29 27 NO",
"25 13 NO",
"19 3 YES",
"14 27 YES",
"11 4 NO",
"26 5 NO",
"28 17 YES" ]


inputB = [
"4 1 0 2 0",
"3",
"0 1 YES",
"0 2 YES",
"0 3 YES"
]


inputBb = [
"4 1 0 2 0",
"3",
"0 1 NO",
"1 2 YES",
"1 3 YES"
]

inputC = [
"10 1 1 2 0",
"27",
"0 6 YES",
"0 2 NO",
"9 3 YES",
"3 7 YES",
"8 0 NO",
"4 0 YES",
"1 3 NO",
"7 9 YES",
"3 2 NO",
"9 1 NO",
"6 9 YES",
"4 5 NO",
"0 9 YES",
"3 8 NO",
"3 5 NO",
"8 5 YES",
"7 4 YES",
"1 2 YES",
"3 6 YES",
"5 9 NO",
"8 6 NO",
"7 1 NO",
"8 1 YES",
"8 4 NO",
"7 0 YES",
"3 4 YES",
"5 2 YES",
]

inputC2 = [
"10 1 1 2 0",
"17",
"1 3 NO",
"0 9 NO",
"0 3 YES",
"2 7 YES",
"0 1 YES",
"0 4 NO",
"1 6 NO",
"2 4 NO",
"1 4 YES",
"0 6 YES",
"0 2 YES",
"2 3 YES",
"2 5 YES",
"1 7 NO",
"0 5 YES",
"2 1 NO",
"0 7 YES"
]

inputCc=[
"10 1 1 2 0",
"20",
"1 7 NO",
"1 4 YES",
"4 3 YES",
"4 2 NO",
"4 9 NO",
"3 7 YES",
"3 2 NO",
"3 1 YES",
"3 6 NO",
"3 5 NO",
"1 9 NO",
"1 5 NO",
"1 2 NO",
"1 0 YES",
"0 4 YES",
"4 7 NO",
"0 7 NO",
"0 2 NO",
"1 6 NO",
"1 8 NO"
]
from tools import input, initArrayInputter
initArrayInputter(inputCc)
from random import randint,seed
seed()
import sys

def try_max(equals, notequals, N, L, K):
    equals_f = sorted([(k, v) for k, v in equals.items()], key=lambda x: len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if (len(equals[As]) > 0 and len(notequals[As]) < len(equals[As])):
            return As
    return None

def try_question(equals, notequals, N, L, K, R):

    loops = N*5
    while loops > 0:
        loops -= 1
        As = try_max(equals, notequals, N, L, K)
        if (As == None):
            As = randint(1,N*(K-1)//(K))-1
        Bs = randint(1,N)-1

        if (Bs == As):
            continue
        if len(notequals[As]) >= N*(K-1)//K - R:
            continue
        if len(notequals[Bs]) >= N*(K-1) //K - R:
            continue

        if As in equals[Bs] or Bs in equals[As]:
            continue
        if As in notequals[Bs] or Bs in notequals[As]:
            continue
        return (As, Bs)
    return None

def tryGuess(equals_s, notequals, N,L, K):
    print(equals_s, file=sys.stderr)
    equals_f = [(k,v) for k,v in equals_s.items() if (len(v) > N//K + L  )]
    if len(equals_f) > 0:
        return equals_f[0][0]
    else:
        return None

def doGuess(equals_s, notequals, N,L, K):

    equals_f = sorted([(k,v) for k,v in equals_s.items()], key=lambda x : len(x[1]), reverse=True)
    for eq_entry in equals_f:
        As = eq_entry[0]
        if (len(equals[As]) > 0 and len(notequals[As]) < len(equals[As])):
            return As
    return None




N, pl_flag, L, K, L_max = map(int, input().split())
D = int(input())
allconds = []

min_guesses = (L + 1) * N / 2

equals, notequals = {k:set() for k in range(N)},{k:set() for k in range(N)}
for i in range(D):
    As, Bs, resp = input().split()
    A, B = int(As), int(Bs)
    allconds.append({"A": A, "B": B, "R": 1 if resp == 'YES' else 0})

for cond in allconds:
    if cond["R"] == 1:
        equals[cond["A"]].add(cond["B"])
        equals[cond["B"]].add(cond["A"])
    else:
        notequals[cond["A"]].add(cond["B"])
        notequals[cond["B"]].add(cond["A"])

while True:
    added = False
    for k,v in equals.items():
        for ve in v:
            if ve not in equals[k]:
                equals[k].add(ve)
                added = True
            if k not in equals[ve]:
                equals[ve].add(k)
                added = True
    if not added:
        break



print("EQUALS ",equals, file=sys.stderr)
print("NOTEQUALS ",notequals, file=sys.stderr)
tg = tryGuess(equals, notequals, N, L, K)
if (tg != None):
    print(tg)
else:
    done = False
    R = 0
    while not done:
        tq = try_question(equals, notequals, N, L, K, R)

        if (tq != None):
            print(tq[0], tq[1])
            done = True
        else:
            tg = doGuess (equals, notequals, N, L, K)
            if (tg != None):
                print(tg)
                done = True
        R += 1