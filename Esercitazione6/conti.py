from analyzer import *
from uncertainties import *

R1 = ufloat(984, mme(984, 'ohm'))
R2 = ufloat(9.95e3, mme(9.95e3, 'ohm'))
C = ufloat(45.4e-9, sqrt(45.4*4/100 + 0.3**2)*1e-9)

f1 = (2*pi*C*R2)**(-1)
f2 = (2*pi*C*R1)**(-1)

print("\nR1 =", R1,"\nR2 =", R2,"\nC =", C)
print("\nfrequenza di taglio integratore:", f1)
print("frequenza di taglio derivatore:", f2) 
print("\n")
