import math
T = 320
e = 9.1
nb = 1
i = 0

while(i<1000):
    m = 8.314/(19.806+0.002095*T*(e**(nb-1)+1))+1
    nb = m
    i = i + 1

print("n =",float(nb))