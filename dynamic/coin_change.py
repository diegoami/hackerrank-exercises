
state = 0
inputarray =[
"4 3",
"1 2 3"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result


sols = {0:[]}


def getWays(n, c):
    print("calling getWays({}) : {}".format(n, c))
    if (n < 0):
        return [[]]
    elif (n in sols):
        return sols[n]
    elif (n == 1):
        soll = [[1]] if 1 in c else []
        sols[n] = soll
        return soll
    else:
        soll = []
        cc = list(c)
        for ci,ce in enumerate(c):
            if (ce == n):
                soll.append([ce])
            elif (ce < n):
                nr = n - ce
                ws = getWays(nr,cc)
                print("{} : retrieving getWays({}) : {}".format(n, nr, ws))

                for w in ws:
                    print("{} : sum({})+{} == {}".format(n, w,ce, n))

                    if sum(w)+ce == n:
                        soll.append(w+[ce])
        sols[n] = soll
        print("returning getWays({}) : {}".format(n,soll))
        return soll


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(set(ways))