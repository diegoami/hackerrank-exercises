import sys
state = 0

#inputarray = ["1 1 1 0 0 0","0 1 0 0 0 0","1 1 1 0 0 0","0 0 2 4 4 0","0 0 0 2 0 0","0 0 1 2 4 0" ]
inputarray = [
"20 23 6"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

f,l,d = map(int, input().split())

cnt = 0
for i in range(f,l+1):
    ri = int(str(i)[::-1])
    if abs(i-ri) % d == 0:
        cnt += 1
print(cnt)