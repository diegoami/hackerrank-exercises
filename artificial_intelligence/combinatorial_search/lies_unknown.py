
inputArray = [
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

from tools import input, initArrayInputter
initArrayInputter(inputArray2)

from random import randint,seed
seed()
import sys
from itertools import product

def gcmb(D, K):

     cart = product(range(K),repeat=D)
     return cart


def return_allowed(pd, conds):
    for p in pd:
        allowed = True
        for cond in conds:
            Ac = cond['A']
            Bc = cond['B']
            Rp = cond['R']
            if (p[Ac] == p[Bc] and not Rp) or (p[Ac] != p[Bc] and Rp):
                allowed = False
                #print('Condition not fulfilled : ', cond)

        if allowed:
            allowedCombs.append(p)
    return allowedCombs
from collections import Counter


def try_answer_2(combs):
    answers = set()
    for comb in combs:
        mcms = Counter(comb).most_common(2)
        if (len(mcms) < 2):
            print("No data", file=sys.stderr)
            return None

        if (mcms[0][1] > mcms[1][1]):
            answers.add(mcms[0][0])
        else:
            print("Found ambigous:", mcms, file=sys.stderr)
            return None
    if len(answers) == 1:
        return answers.pop()
    else:
        print("Too many answers:", answers, file=sys.stderr)
        return None


def try_answer(combs):
    answers = []
    for comb in combs:
        print("Processing comb", comb, file=sys.stderr)
        mcms = Counter(comb).most_common()
        if (len(mcms) < 1):
            print("No data", file=sys.stderr)
            continue
        else:
            color = comb.index(mcms[0][0])
            answers.add(color)

    if len(answers) == 1:
        return answers.pop()
    else:
        answer = Counter(answers).most_common()

        print("Giving answer:", answer[0], file=sys.stderr)





def generate_possible_question(combs,N):

    loops = N
    while loops > 0:
        loops -= 1
        As = randint(1,N)-1
        Bs = randint(1,N)-1

        if (Bs == As):
            continue
        foundDiff, foundEqual = False, False
        for c in combs:
            if c[Bs] != c[As]:
                foundDiff = True
            else:
                foundEqual = True

        if (foundDiff and foundEqual):
            return (As,Bs)
        else:
            print("Unnecessary question: {}, {}".format(As,Bs), file=sys.stderr)

    return None

from itertools import combinations
N, pl_flag, L, K, L_max = map(int,input().split())
D = int(input())
allconds = []

for i in range(D):
    As,Bs,resp = input().split()
    A,B = int(As)-1, int(Bs)-1
    allconds.append({"A":A, "B":B, "R":1 if resp == 'YES' else 0 })


pd = gcmb(N,K)
allowedCombs = []
ACL = len(allconds)
cmbs = combinations(allconds,ACL-L)
#print(cmbs)
answers = []
for conds in cmbs:
#    print(conds)
    allowed_combs = return_allowed(pd, conds)
    possible_question = generate_possible_question(allowed_combs,N)
    if possible_question == None:

        answer = try_answer(allowed_combs)
        answers.append(answer)
    else:
        print(possible_question[0], possible_question[1] )
        break
