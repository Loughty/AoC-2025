dial  = 50
ceros = 0

print("number goes from 0 to 99, 99 right goto 0, and 0 left goto 99")
print("its like a decimal clock...")
print("dial current position: ", dial)

# rotations = [\
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
    dial = dial + x
#    print("calculo: ", dial)
    if dial >= 100:
        dial = dial - 100
        print("full circle to right")
    if dial < 0:
        dial = 100 + dial
        print("full circle to left")
    if dial == 0:
        ceros = ceros + 1
    print("resultado: ", dial)

print("total of ceros: ", ceros)