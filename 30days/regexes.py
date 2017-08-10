#!/bin/python3


inputarray = [
"6",
"riya riya@gmail.com",
"julia julia@julia.me",
"julia sjulia@gmail.com",
"julia julia@gmail.com",
"samantha samantha@gmail.com",
"tanya tanya@gmail.com"
]

from tools import input, initArrayInputter
initArrayInputter(inputarray)

import re
N = int(input().strip())
names = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    m = re.search('[a-z]+@gmail\.com',emailID)
    if m:
        names.append(firstName)
print(*sorted(names),sep='\n')