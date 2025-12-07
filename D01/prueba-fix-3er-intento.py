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
#for x in rotations:
    if x >= 0: dial = (dial + x)%100
    else:
        dial = (dial + x)%100
        while dial < 0: dial = dial + 100
    if dial == 0: ceros = ceros + 1

print("total of ceros: ", ceros)