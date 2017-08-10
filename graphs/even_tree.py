

inputarray = [
"10 9",
"2 1",
"3 1",
"4 3",
"5 2",
"6 1",
"7 2",
"8 6",
"9 8",
"10 8"
]



from tools import input, initArrayInputter
initArrayInputter(inputarray)

import graphs
T = graphs.Tree()
N,M = map(int, input().split())
for i in range(M):
    v1,v2 = input().split()
    T.addEdge(v1,v2)
#T.doPrint()
print(T.walk_tree()[1])