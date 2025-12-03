# esta solucion creo que me puede dar el resultado correcto
# pero creo que está redondeando mal, el resultado que da es 64

dial  = 50
ceros = 0

print("number goes from 0 to 99, 99 right goto 0, and 0 left goto 99")
print("its like a decimal clock...")
print("dial current position: ", dial)

# deberia darte tres ceros de resultado
# rotations = [
#     -68,
#     -30,
#      48,
#     -5,
#      60,
#     -55,
#     -1,
#     -99,
#      14,
#     -82,
# ]

import list

#print("minus is left: ", rotations)
print("minus is left: ", list.rotations)

for x in list.rotations:
    print("posición actual: ", dial)
    print("rotación (negativo es izquierda): ", x)
    integral, decimal = divmod((dial + x)/100, 1)
    print("integral: ", integral, "decimal: ", decimal)
    if integral < 0: print("giró ", integral, " veces a la izquierda")
    if integral > 0: print("giró ", integral, " veces a la derecha")
    dial = int(decimal * 100)
    print("posición actual: ", dial)
    if dial == 0: ceros = ceros + 1

print("total of ceros: ", ceros)