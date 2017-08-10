
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


from tools import input, initArrayInputter
initArrayInputter(inputArray6)

from random import randint,seed
seed()
import sys
from itertools import product

def generate_some_tuples(D, K):
    for _ in range(5000):
        ball_combo = []
        for d in range(D):
            k = randint(1,K)-1
            ball_combo.append(k)
        yield ball_combo

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
#                print('Condition not fulfilled : ', cond, p, file=sys.stderr)
                break

        if allowed:
            allowedCombs.append(p)
    return allowedCombs
from collections import Counter




def get_answers(combs):
    answers = []
    for comb in combs:
#        print("Processing comb", comb, file=sys.stderr)
        mcms = Counter(comb).most_common()
        color = mcms[0][0]
        if (len(mcms) < 1):
#            print("No data", file=sys.stderr)
            continue
        else:

#            print("Retrieved color ", color, file=sys.stderr)

            ball = list(comb).index(color)
#            print("Retrieved ball ", ball, file=sys.stderr)

            answers.append(color)


    return answers





def generate_possible_question(combs,N):

    loops = N*5
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
#        else:
#           print("Unnecessary question: {}, {}".format(As,Bs), file=sys.stderr)

    return None

from itertools import combinations
N, pl_flag, L, K, L_max = map(int,input().split())
D = int(input())
allconds = []

for i in range(D):
    As,Bs,resp = input().split()
    A,B = int(As), int(Bs)
    allconds.append({"A":A, "B":B, "R":1 if resp == 'YES' else 0 })



allowedCombs = []
ACL = len(allconds)
cmbs = combinations(allconds,max(ACL-L,0))
#print(cmbs)
answers = []
question_asked = False
for conds in cmbs:
#    print(conds,file=sys.stderr)
    pd = generate_some_tuples(N,K)
    allowed_combs = return_allowed(pd, conds)
    possible_question = generate_possible_question(allowed_combs,N)
    if possible_question == None:

        answers = answers + get_answers(allowed_combs)

    else:
        print(possible_question[0], possible_question[1] )
        question_asked = True
        break
if (question_asked == False):
    if len(answers) > 0:
        print(Counter(answers).most_common()[0][0])
    else:
        for X in range(ACL-L):

            cmbs = combinations(allconds, max(ACL - L - X, 0))

            for conds in cmbs:
                #print(conds,file=sys.stderr)
                pd = generate_some_tuples(N, K)
                allowed_combs = return_allowed(pd, conds)
                #print(allowed_combs ,file=sys.stderr)
                answers = answers + get_answers(allowed_combs)
            if (len(answers) > 0):
                #print(Counter(answers).most_common()[0][0])
                break