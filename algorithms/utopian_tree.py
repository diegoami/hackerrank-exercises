
state = 0


inputarray = [
"3",
"0",
"1",
"4"
]
def input():
    global state
    result = inputarray[state]
    state += 1
    return result

def ut_tree(n):
    if n <= 0:
        return 1
    else:
        return 2*ut_tree(n-1) if n % 2 == 1 else 1+ut_tree(n-1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ut_tree(n))