from analyzer import *
from uncertainties import *
Vbe = ufloat(0.625, 0.004)
Vcc = ufloat(19.85, 0.11)
R1 = ufloat(177.1e3, 1.5e3)
R2 = ufloat(18.06e3, 0.15e3)
RE = ufloat(986, 9)
RC = ufloat(9.93e3,0.09e3)
Vb = Vcc*R2/(R1+R2)
Ic = (Vb-Vbe)/RE
Vout = Vcc - Ic*RC
Rb = R1*R2/(R1+R2)
Ib = (Vb-Vbe)/Rb
Ib_h = (Vb-Vbe)/(Rb+100*RE)
Ib_l = (Vb-Vbe)/(Rb+300*RE)
Ic = 100 * Ib_h
Vout = Vcc - Ic*RC
