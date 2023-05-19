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

        # Emitir el par clave-valor: productid y title como clave y score como valor
        key = [productid, title]

        if score != "empty":
            print("{0}\t{1}".format(key, score))
