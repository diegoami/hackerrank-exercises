inputarray = [
"5",
"47"
]
state = 0
def input():
    global state
    result = inputarray[state]
    state += 1
    return result




hn = [ \
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"one"
]

mn = \
[
"o' clock",
"one minute",
"two minutes",
"three minutes",
"four minutes",
"five minutes",
"six minutes",
"seven minutes",
"eight minutes",
"nine minutes",
"ten minutes",
"eleven minutes" ,
"twelve minutes",
"thirteen minutes",
"fourteen minutes",
"quarter",
"sixteen minutes",
"seventeen minutes",
"eighteen minutes",
"nineteen minutes",
"twenty minutes",
"twenty one minutes",
"twenty two minutes",
"twenty three minutes",
"twenty four minutes",
"twenty five minutes",
"twenty six minutes",
"twenty seven minutes",
"twenty eight minutes",
"twenty nine minutes",
"half"
]





h = int(input().strip())
m = int(input().strip())

if (m == 0):
    print(hn[h]+ ' '+mn[m])
elif (m <= 30):
    print(mn[m] + ' past ' + hn[h])
else:
    print(mn[60-m] + ' to ' + hn[h+1])
