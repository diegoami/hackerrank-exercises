import itertools as it

#sf = ['A','B','C','D','E','F','G','H','I','J']
sf = ['A','B','C','D']

sfp = it.permutations(sf)
cp = 0
ct = 0
for pfpi in sfp:
    cp += 1
    pfp = list(pfpi)
    pfp.append(pfp[0])
    pfps = ''.join(pfp)
    ia = pfps.find('AB')
    ib = pfps.find('BA')
    if (ia + ib > -2):
        print('Y', pfps)
        ct += 1
    else:
        print('N', pfps)

print(cp,ct)

#(2*(n-2)!*(n-1))/n! = 2/n
#(2*(n-2)!*(n-1)! = 2/(n-1)