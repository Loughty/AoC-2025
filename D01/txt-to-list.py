## process the input.txt, so i can used it has a list
## the result must stored on "list.py" and loaded on "prueba.py"

with open("input.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)

with open('list.py', 'w') as lista:
#    lista.write("rotations = [\\")
    lista.write("rotations = [")
    lista.write("\n")
    for x in contenido:
        if x == 'L': lista.write("-")
        elif x == 'R': pass
        elif x == "\n":
            lista.write(",")
            lista.write("\n")
        else: lista.write(x)
    lista.write("]")
