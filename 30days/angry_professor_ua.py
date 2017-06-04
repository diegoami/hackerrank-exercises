state = 0

inputarray = [
"2",
"4 3",
"-1 -3 4 2",
"4 2",
"0 -1 2 1"
]



def input():
    global state
    if (state < len(inputarray) ):
        result = inputarray[state]
        state += 1
        return result
    else:
        return None
import sys

def print_array():
    global state
    state = 0
    while True:
        x = input()
        if x:
            print(x)
        else:
            break


def expect_output():
    global state
    state = 0

    eo = []
    t = int(input().strip())

    for a0 in range(t):
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        a = [int(a_temp) for a_temp in input().strip().split(' ')]
        s_i_t = [x for x in a if x <= 0]
        eo.append("YES" if len(s_i_t) < k else "NO")
    return eo


#es = expect_output()
print_array()
#print(*expect_output(),sep='\n')

