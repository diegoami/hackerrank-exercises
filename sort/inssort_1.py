state = 0

inputarray = [
"5",
"2 4 6 8 3"
]



def input():
    global state
    result = inputarray[state]
    state += 1
    return result



def insertion_sort(m):
    e = m[-1]

    l = m[:-1]
    index = len(l)-1
    while l[index] > e and index >= 0:
        l = (m[:index]+[m[index],m[index]]+m[index+1:])[:len(m)]
        print(" ".join(map(str, l)))
        index -= 1
    l = (m[:index+1]+[e]+m[index+1:])[:len(m)]
    print(" ".join(map(str, l)))


def insertion_sort2(m):
    l = list(m)
    e = l[-1]
    #print(e)
    for i in range(len(l)-2,-1,-1):

     #   print(i)
        if e < l[i]:
            #print(len(l))
          #  print(l[i+1])
            del(l[i+1])
            l.insert(i,l[i])
            print(" ".join(map(str, l)))
        else:
            del (l[i+1])
            l.insert(i+1, e)

            print(" ".join(map(str,l)))
            break


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
#print(ar)
insertion_sort(ar)
