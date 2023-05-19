input_file = "Video_Games.txt"
output_file = "Video_Games_formatted.txt"

with open(input_file, "r") as input, open(output_file, "w") as output:
    for line in input:
        line = line.strip()
        if line.startswith("product/") or line.startswith("review/"):
            fields = line.split(": ")
            key = fields[0]
            if len(fields) > 1:
                value = fields[1]
            else:
                value = "Empty"  # Si el valor está vacío
            output.write(value + "\t")  # Tabulador
        else:
            output.write("\n")  # Agrega una nueva línea después de cada reseña

print("Conversión de formato completada. Resultado guardado en", output_file)
