

inputarray =[
"0 1 5"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)


cfc = {}
def cfibm(t, t1, t2):
    if t in cfc:
        return cfc[t]
    else:
        if t == 1:
            res = t1
        elif t == 2:
            res = t2
        else:
            res = cfibm(t - 2, t1, t2) + cfibm(t - 1, t1, t2) ** 2
        cfc[t] = res
        return res


t1,t2,t = map(int, input().split())
print(cfibm(t,t1,t2))
