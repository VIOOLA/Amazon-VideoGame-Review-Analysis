#!/usr/bin/python

import sys
import string

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

        # Reemplazar los signos de puntuación y dígitos por espacios y convertir todo a minúsculas
        exclude = string.punctuation + string.digits
        for char in exclude:
            text = text.replace(char, " ")
        text = text.lower()

        words = text.split()

        for word in words:
            print("{0}\t{1}".format(word, 1))
