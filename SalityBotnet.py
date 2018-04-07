import sys
import csv #import csv library
import datetime
import time
import matplotlib.pyplot as pp
from datetime import timedelta
import pandas as pd
f = open('/home/rashad/data/DATASET/FLOWS/sality_filtered_udp.binetflow') #open csv file and 
csv_f = csv.reader(f)
next(csv_f, None)
#for row in csv_f:
#    
#    date = datetime.datetime.strptime (row[0],"%Y/%m/%d %H:%M:%S.%f")
#    count += 1
#    print date
#print count
rows = list(csv.reader(f))
list_len = len(rows)
print list_len
myList = []
count = 0
flowGroup = [0]
        
for line in rows:
    if count == list_len -1:
        break
    else:
        date1 = datetime.datetime.strptime (rows[count][0],"%Y/%m/%d %H:%M:%S.%f").strftime("%s")
        date2 = datetime.datetime.strptime (rows[count+1][0],"%Y/%m/%d %H:%M:%S.%f").strftime("%s")
    count += 1
    diff = int(date2) - int(date1)
    myList.append(diff)
    
    if diff > 2000:
    #if diff < 200 and diff > 100:
        flowGroup.append(count)
        #print diff, count, rows[count-1][0], rows[count+1][0]
    else:
        pass

#print len(myList)
#print rows[8335:8337]
#print myList[0:987], myList[988], myList[989:2000]
#print myList

#print flowGroup
x = 0
flowDict = []

#while x < len(flowGroup):
#    if x == len(flowGroup) - 1:
#        break
#    else:
#        flowDict.append(rows[(flowGroup[x]):(flowGroup[x+1])])
#        #print rows[(flowGroup[x]):(flowGroup[x+1])]
#    x += 1

#col_a = [flowDict[0][1][6] for row in flowDict]
#col_b = [flowDict[0][0][6] for row in flowDict]
#only_a = [pid for pid in col_a if not pid in col_b]
#only_b = [pid for pid in col_b if not pid in col_a]
for x in xrange(len(flowGroup)):
    if x == len(flowGroup) - 1:
        break
    else:
        flowDict.append(rows[(flowGroup[x]):(flowGroup[x+1])])
for m in xrange(len(flowDict)):
    print "iteration###############################################:", m
    for y in xrange(len(flowDict[m])):
        print flowDict[m][y][6]

