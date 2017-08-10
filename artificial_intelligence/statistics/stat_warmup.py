

inputarray = [
    "10",
    "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
]
from tools import input, initArrayInputter
initArrayInputter(inputarray)


def ecdf(data):
    """Do not replace this"""
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n

    n = len(data)
    # x-data for the ECDF: x

    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1,n+1) / n

    return x, y

import numpy as np, scipy.stats as st
import math
n = int(input())
rn = list(map(float, input().split()))
a = np.array(rn)
mn,std =np.mean(a), np.std(a)
sqrtn = math.sqrt(n)
print("{:.1f}".format(mn).rstrip('0').rstrip('.'))
print("{:.1f}".format(np.median(a)).rstrip('0').rstrip('.'))
print("{:.1f}".format(float(np.mean(st.mode(a).mode))).rstrip('0').rstrip('.'))
print("{:.1f}".format(float(std)).rstrip('0').rstrip('.'))
#intrv = st.norm.interval([0.025,0.975], loc=np.median(a), scale=np.std(a)/len(a))
#intrv = st.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=st.sem(a))

z1,z2 = mn - 1.96*std/sqrtn, mn + 1.96*std/sqrtn,#
percentiles =  np.array([2.5,50,97.5])
#print(st.scoreatpercentile(a, [2.5,97.5]))
#print(np.percentile(a,percentiles,axis=0))
print("{:.1f} {:.1f} ".format(z1,z2))
