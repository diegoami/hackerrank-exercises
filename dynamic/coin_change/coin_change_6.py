


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

# Initialize an array of combination numbers for all target_money amounts from 0 until the amount you want to reach
# For each coin:
#   loop all money values from the coin value until the target money amount:
#       for all money values
#           get the number of combinations for the money value minus the coin value
#           add this to the number of combinations of the current value, because you can construct it just adding the coin value to those combinations

from tools import input, initArrayInputter
initArrayInputter(inputarray2)

# Initialize an array of combination numbers for all target_money amounts from 0 until the amount you want to reach
# For each coin:
#   loop all money values from the coin value until the target money amount:
#       for all money values
#           get the number of combinations for the money value minus the coin value
#           add this to the number of combinations of the current value, because you can construct it just adding the coin value to those combinations

import sys
target_money, coin_count = input().strip().split(' ')
target_money, coin_count = [int(target_money), int(coin_count)]
coins = list(map(int, input().strip().split(' ')))
combinations = [1] + [0] * target_money

for coin_index in range(coin_count):
    print("Combinations before processing coin {}: {}".format(coins[coin_index], combinations), file=sys.stderr)
    for money in range(coins[coin_index], target_money + 1):
        if (combinations[money - coins[coin_index]]) > 0:
            print("    Combinations for {} added to combinations for {} : {} += {}".format(money - coins[coin_index], money, combinations[money], combinations[money - coins[coin_index]]), file=sys.stderr)
            combinations[money] += combinations[money - coins[coin_index]]
    print("Combinations after processing coin {}: {}".format(coins[coin_index], combinations), file=sys.stderr)

print("Combinations for {} : {}".format(target_money, combinations[target_money]), file=sys.stderr)
print(combinations[-1])