

inputarray = [
"5",
"2 4 6 8 3"
]

inputarray2 = [
"6",
"1 4 3 5 6 2"
]


from tools import input, initArrayInputter
initArrayInputter(inputarray2)

def insertion_sort(m,e):
    #print(m,e)
    l = list(m)
    index = len(l)-1
    while any([l[i] > e for i in range(index+1)] ) and index >= 0:
        l = (m[:index]+[m[index],m[index]]+m[index+1:])

        index -= 1
        #print(l,index)
    l = (m[:index+1]+[e]+m[index+1:])
    #print(l)
    return l


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]

r = ar
for i in range(1,len(ar)):
    e = ar[i]
    if (any([r[j] > e for j in range(i+1)])):
        r = insertion_sort(r[:i]+r[i+1:], e)
    print(" ".join(map(str, r)))