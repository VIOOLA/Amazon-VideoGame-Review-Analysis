#!/usr/bin/python

import sys

current_productid = None
score_sum = 0
count = 0

for line in sys.stdin:
    productid, score = line.strip().split("\t")

    if current_productid and current_productid != productid:
        # Calcular el score promedio y emitir el resultado
        if count >= 10:
            average_score = score_sum / count
            print("{0}\t{1}".format(current_productid, round(average_score, 2)))

        score_sum = 0
        count = 0

    # Actualizar el producto actual y acumular el score y cuenta el numero
    current_productid = productid
    score_sum += float(score)
    count = count + 1

# Calcular el score promedio para el último producto
if current_productid:
    if count >= 10:
        average_score = score_sum / count
        print("{0}\t{1}".format(current_productid, round(average_score, 2)))
