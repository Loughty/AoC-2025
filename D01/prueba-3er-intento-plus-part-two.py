## THIS SOLUTION IS NOT WORKING FOR DAY 01 PART II
## PROBABLY THE REASON IS AROUND THE WAY IT COUNTS THE CEROS...
## ... WHEN IT ALREADY ON DIAL 0, CHECK THAT AND FIX IT

## if i leave it at it is, the answer give a number too hight

## if i subtract 1 to the cero count, it gives a number too low

## if i subtract or sum depending if is positive or negative...
## ... the result is almost the same has the first test, but...
## ... with slighly higher number

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
