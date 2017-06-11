state = 0

inputarray = [
"4",
"aba",
"baba",
"aba",
"xzxb",
"3",
"aba",
"xzxb",
"ab"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result



n = int(input().strip())
S = []
for i in range(n):
    S.append(input().strip())

Q = []
qn = int(input().strip())
for i in range(qn):
    qs = input().strip()
    ff = 0
    for s in S:
        if s == qs:
            ff += 1

    print(ff)