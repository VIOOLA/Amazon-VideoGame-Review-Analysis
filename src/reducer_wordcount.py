#!/usr/bin/python

import sys

wordCounts = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, count = data_mapped

    if thisWord in wordCounts:
        wordCounts[thisWord] += int(count)
    else:
        wordCounts[thisWord] = int(count)

# Output the word counts for words with more than 4 occurrences
for word, count in wordCounts.items():
    if count > 4:
        print("{0}\t{1}".format(word, count))
