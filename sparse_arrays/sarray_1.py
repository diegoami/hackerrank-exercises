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
S = [input().strip() for i in range(n)]
qn = int(input().strip())
for _ in range(qn):
    print(sum([S.count(input().strip())]))