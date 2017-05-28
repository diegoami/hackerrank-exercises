
state = 0

inputarray = [
"4",
"abc",
"abcba",
"abcd",
"cba"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result


def get_distance(s):
    r = s[::-1]
    d = 0
    for i in range(len(s)//2):
        d += abs(ord(r[i])-ord(s[i]))
    return d

n = int(input().strip())
cs = None
for i in range(n):
    c = input().strip()
    print(get_distance(c))