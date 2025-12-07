# esta solucion creo que me puede dar el resultado correcto
# pero creo que está redondeando mal, el resultado que da es 64

dial  = 50
ceros = 0

print("number goes from 0 to 99, 99 right goto 0, and 0 left goto 99")
print("its like a decimal clock...")
print("dial current position: ", dial)

# deberia darte seis como resultado (veces que paso por el cero)
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

print("minus is left: ", list.rotations)
for x in list.rotations:
#print("minus is left: ", rotations)
#for x in rotations:
    if x >= 0:
        ceros = ceros + ((dial+x)//100)
        dial = (dial + x)%100
    else:
        ceros = ceros + (((dial+x)//100)*-1)
        dial = (dial + x)%100
        while dial < 0: dial = dial + 100

print("total of ceros: ", ceros)

## dice que la respuesta no es correcta
## que es muy alta...
## el ejemplo que dan no es suficiente
## así que no me molestare en adivinar