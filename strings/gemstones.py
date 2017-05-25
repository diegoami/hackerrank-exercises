
state = 0

inputarray = [
"3",
"abcdde",
"baccd",
"eeabg"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result

def funny(s):
    r = s
    r = s[::-1]
    for i in range(1,len(s)):
        if abs (ord(s[i]) - ord(s[i-1]) )  !=  abs (ord(r[i]) - ord(r[i-1]) ) :
            print("Not Funny")
            return
    print("Funny")



n = int(input().strip())
cs = None
for i in range(n):
    c = input().strip()
    s = set(list(c))
    cs = s if cs == None else s.intersection(cs)

print(len(cs))