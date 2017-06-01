
state = 0
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




def input():
    global state
    result = inputarray[state]
    state += 1
    return result


sols = {}




def getWays(n, c, index):
    #print("calling getWays({}) : {}".format(n, c))
    if (n < 0):
        return {}
    elif ((n,index) in sols):
        return sols[(n,index)]
    else:
        soll = 0
        cc = list(c)
        for ci,ce in enumerate(c,index):
            if (ce == n):
                soll += 1
                break;
            elif (ce < n):
                nr = n - ce
                ws = getWays(nr,cc,index+1)
                soll += ws

        sols[(n,index)] = soll
        #print("returning getWays({}) : {}".format(n,soll))
        return soll


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
cf = sorted(c,reverse=True)
#print(cf)
ways = getWays(n, cf, 0)
print(ways)