from analyzer import *
from uncertainties import *

gm = ufloat(4e-3, 0.05e-3)
RS = ufloat(244 , 3)
RD = ufloat(985, 9)

A1 = gm*RD/(1+gm*RS)
A2 = gm*RS/(1+gm*RS)

print (A1,"\n",A2)