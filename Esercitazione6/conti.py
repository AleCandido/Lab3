from analyzer import *
from uncertainties import *

DV = ufloat(9.44, 9.44*0.025)
Dt = ufloat(740e-9, 7.4e-9)

slew = DV/Dt

R1 = ufloat(984, mme(984, 'ohm'))
R2 = ufloat(9.95e3, mme(9.95e3, 'ohm'))
C = ufloat(45.4e-9, sqrt(45.4*4/100 + 0.3**2)*1e-9)

A1 = R2/R1
A2 = ufloat(9.72,0.08)

V1=ufloat(2.88,2.88*0.035)
V2=ufloat(1.44,1.44*0.035)
RS=ufloat(9.96e3,0.09e3)

RIN = (V1-V2)*RS/V2

fsq = ufloat(9.722e3, 97.22)
Vsqin = ufloat(1.26, 1.26*0.025)
Vsqom = ufloat(936e-3, 936e-3*0.025)

Vsqo = Vsqin*2*pi/(2*fsq*R2*C)
Vsqe = Vsqin*(1-e**(-2*pi/(2*fsq*R2*C)))

DVsl = ufloat(22.6, 22.6*0.025)
Dtsl = ufloat(2.06e-6, 2.06e-8)

maxv = DVsl/Dtsl

f1 = (2*pi*C*R2)**(-1)
f2 = (2*pi*C*R1)**(-1)

print("\n")
print("DV = ", DV,"\nDt =", Dt,"\nslew rate:", slew, "\n")
print("R1 =", R1,"\nR2 =", R2,"\nC =", C)
print("\nVsq output =", Vsqo, "\nVsqe =", Vsqe)
print("\nmassima pendenza in uscita =", maxv)
print("\nfrequenza di taglio integratore:", f1)
print("frequenza di taglio derivatore:", f2) 
print("\n")
