import sys
from math import *
from random import *

temp = sys.argv[1]
darts = int(temp) + 1

inCirc = 0
outCirc = 0

for dart in range(darts):
    x = randrange(-1.0,1.0)
    y = randrange(-1.0,1.0)
    z = (x * x) + (y * y)
    dist = sqrt(z)

    if dist > 1.0:
        outCirc = outCirc + 1
    else:
        inCirc = inCirc + 1

final = inCirc/outCirc

print("pi estimate = ", final)
