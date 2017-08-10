

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
initArrayInputter(inputarray)




n, m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [1]+[0]*n
for i in range(m):
    for j in range(coins[i], n+1):
        dp[j] += dp[j-coins[i]]
print(dp[-1])