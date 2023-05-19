#!/usr/bin/python

import sys

oldKey = None
count = 0

for line in sys.stdin:
    thisKey = line.strip().split("\t")[0]

    if oldKey and oldKey != thisKey:  # nuevo producto
        print("{0}\t{1}".format(oldKey, count))
        count = 0

    oldKey = thisKey
    count = count + 1

if oldKey:
    print("{0}\t{1}".format(oldKey, count))
