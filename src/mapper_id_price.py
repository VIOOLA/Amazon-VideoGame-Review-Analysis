#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 10:
        (
            productid,
            title,
            Price,
            userId,
            profileName,
            helpfulness,
            score,
            time,
            summary,
            text,
        ) = data

        key = [productid, title]

        if Price != "unknown" and Price != "empty":
            print("{0}\t{1}".format(key, Price))
