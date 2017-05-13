#!/bin/python3

import sys


time = input().strip()
hour,minute,second,am_pm = time[:2],time[3:5],time[6:8],time[8:]
hour_m = hour if (am_pm == 'AM' or ( am_pm == 'PM' and hour == '12')) else ( "00" if hour =="12" else str(int(hour)+12))  
print("%s:%s:%s" % (hour_m,minute,second))
