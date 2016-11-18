from analyzer import *
from uncertainties import *

R1 = ufloat(9.89e3, 0.09e3)
R2 = ufloat(98.5e3, 0.9e3)

A1 = R2/R1

#print(A1)

A2 = ufloat(9.72,0.08)

#print(A2-A1)

V1=ufloat(2.88,2.88*0.035)
V2=ufloat(1.44,1.44*0.035)
RS=ufloat(9.96e3,0.09e3)

RIN = (V1-V2)*RS/V2

print(RIN)