from itertools import groupby
import numpy as np
import pandas as pd
import anaconda_navigator

import collections


def unique(list1):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list


df = pd.DataFrame(testlist)
grouped = df.groupby(testlist)
print(unique(testlist))
np.unique(np.array(testlist))


testlist = [3, 3, 3, 2, 2, 3, 2, 3, 2, 3, 4, 4, 4, 4]
testlist2 = testlist
sample = []
sample2 = []


def getunorderedlist(counts):
    originalcount = counts[:]
    returncount = []

    for count in originalcount:
        # print(originalcount)
        getnumberindex = [i for i, v in enumerate(originalcount) if v == count]
        print(originalcount)
        for i, j in zip(range(count), getnumberindex):
            returncount.append(originalcount[j])
        for j in range(count):
            #print(count, range(count))
            originalcount.remove(count)
        print(range(count), originalcount)
    return returncount


print(testlist2)
print(testlist)
print(getunorderedlist(testlist[:]))
print(testlist2)
print(testlist)


for key, item in groupby(getunorderedlist(testlist)):
    sample.append(key)
    sample2.append(int(len(list(item))/key))

print(sample)
print(sample2)

sample3 = []
for i in sample:
    for position, item in enumerate(testlist):
        print(item, i)
        if item == i:
            sample3.append(position)

print(sample3)
print(sample3[1:1])
print(sample3[1:2])

sample4 = []
for i, j in zip(sample, sample2):
    for k in range(j):
        sample4.append(sample3[0:i])
        for l in range(i):
            sample3.pop(0)
for i in sample4:
    for j in i:
        print(j, end=" ")
    print()


def socialGraphs(counts):
    counts.pop(0)
    testlist = counts
    sample = []
    sample2 = []

    for key, item in groupby(sorted(testlist)):
        sample.append(key)
        sample2.append(int(len(list(item))/key))

    sample3 = []
    for i in sample:
        for position, item in enumerate(testlist):
            if item == i:
                sample3.append(position)

    sample4 = []
    for i, j in zip(sample, sample2):
        for k in range(j):
            sample4.append(sample3[0:i])
            for l in range(i):
                sample3.pop(0)

    for i in sample4:
        print()
        for j in i:
            print(j, end=" ")
