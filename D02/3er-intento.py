# necesitas encontrar patrones dentro de los rangos de números
# los patrones que encuentres deberás sumarlo
# el resultado de esa suma será tu respuesta
# ejm: 11+22+99+1010+1188511885+222222+446446+38593859 = 1227775554

## procesando el archivo

lista_de_listas = []

with open("input.txt", "r") as input:
    entrada = input.read()
print("\n", entrada)

grupos = entrada.split(",")
print("\n", grupos)

for x in grupos:
    if "-" in x:
        inicio, fin = map(int, x.split("-"))
        lista_rangos = list(range(inicio, fin + 1))
        lista_de_listas.append(lista_rangos)
 
print("\n", lista_de_listas)
print("\n", lista_rangos)


## detectando patrones

## THIS VARIABLE WAS MADE WITH AI, CAUSE I DONT KNOW HOW TO DETECT PATTERNS
def detectar_patron(numero):
    s = str(numero)
    n = len(s)
    
    # 1. La longitud total (n) debe ser par para que se repita dos veces.
    if n % 2 != 0:
        return False
    
    # 2. Calcular la longitud de la mitad del número.
    mitad = n // 2
    
    # 3. Dividir la cadena en dos mitades.
    primera_mitad = s[:mitad]
    segunda_mitad = s[mitad:]
    
    # 4. Verificar si las dos mitades son idénticas.
    if primera_mitad == segunda_mitad:
        return True
    else:
        return False

## CREATE THE LIST OF PATTERN AND MAKE THE TOTAL
lista_patron = set()

for x in lista_de_listas:
    for numero in x:
        if detectar_patron(numero):
            lista_patron.add(numero)

print("\n", lista_patron)

suma = sum(lista_patron)
print("\n la suma de todos los patrones da como resultado: ", suma)