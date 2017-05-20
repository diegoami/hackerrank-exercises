import itertools as it

#sf = ['A','B','C','D','E','F','G','H','I','J']
sf = ['A','B','C','D']

sfp = it.permutations(sf)
cp = 0
ct = 0
for pfp in sfp:
    cp += 1
    ia = pfp.index('A')
    ib = pfp.index('B')
    #if (ia == 0):
    #    ia = len(sf)
    #if (ib == 0):
    #    ib = len(sf)
    if (abs(ia-ib) == 1 or abs(ia-ib) == len(sf)-1):
        print('Y', ''.join(pfp))
        ct += 1
    else:
        print('N', ''.join(pfp))

print(cp,ct)

#(2*(n-2)!*(n-1))/n! = 2/n
#(2*(n-2)!*(n-1)