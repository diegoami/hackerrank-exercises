

inputarray =[
"4 3",
"1 2 3"
]

inputarray2 =[
"10 4",
"2 5 3 6"
]

inputarray3 =[
"69 29",
"25 27 40 38 17 2 28 23 9 43 18 49 15 24 19 11 1 39 32 16 35 30 48 34 20 3 6 13 44",
]




from tools import input, initArrayInputter
initArrayInputter(inputarray2)


sols = {0:[]}




def getWays(n, c):
    #print("calling getWays({}) : {}".format(n, c))
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
                ws = getWays(nr,cc[ci:])
                #print("{} : retrieving getWays({}) : {}".format(n, nr, ws))

                for w in ws:
                    #print("{} : sum({})+{} == {}".format(n, w,ce, n))

                   nls = sorted(w + [ce])
                   if not nls in soll:
                        soll.append(nls)
        sols[n] = soll
        #print("returning getWays({}) : {}".format(n,soll))
        return soll


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
cf = sorted(c,reverse=True)
print(cf)
ways = getWays(n, cf)
print(len(ways))