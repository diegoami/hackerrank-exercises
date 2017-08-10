

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
initArrayInputter(inputarray3)

import functools


solutions = {}

def solve(money,index):
    if str(money)+"-"+str(index) in solutions:
        return solutions[str(money)+"-"+str(index)]
    elif money == 0:
        return 1
    elif money < 0:
        return 0
    elif index >= len(coins):
        return 0
    else:


        amount = 0
        total_result = 0
        while amount <= money :
            remaining = money-amount
            total_result += solve(remaining,index+1 )
            amount += coins[index]


        solutions[str(money)+"-"+str(index)] = total_result
        return total_result

money, m = input().strip().split(' ')
money, m = [int(money), int(m)]
coins = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
print(solve(money,0))