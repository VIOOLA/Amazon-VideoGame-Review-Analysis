input_file = "Video_Games_formatted.txt"
output_file = "Video_Games_reviews.txt"

lineas_vistas = set()
lineas_duplicadas = []

i = 0

with open(input_file, "r") as input, open(output_file, "w") as output:
    for line in input:
        i = i + 1
        if line not in lineas_vistas:
            lineas_vistas.add(line)
            output.write(line)
        else:
            lineas_duplicadas.append(i)

print("Líneas duplicadas eliminadas. Resultado guardado en", output_file)
print("Líneas duplicadas:", lineas_duplicadas)
