


inputarray = [
"2",
"acxz",
"bcxz"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

def funny(s):
    r = s
    r = s[::-1]
    for i in range(1,len(s)):
        if abs (ord(s[i]) - ord(s[i-1]) )  !=  abs (ord(r[i]) - ord(r[i-1]) ) :
            print("Not Funny")
            return
    print("Funny")



n = int(input().strip())

for i in range(n):
    c = input().strip()
    funny(c)