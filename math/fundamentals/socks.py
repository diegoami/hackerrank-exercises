
state = 0

inputarray = [
"2",
"1",
"2"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

n = int(input())
for i in range(n):
    sks = int(input())
    print(sks+1)