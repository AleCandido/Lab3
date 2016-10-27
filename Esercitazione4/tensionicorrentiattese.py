from analyzer import *
from uncertainties import *

# misure effettuate

Vbe = ufloat(0.625, 0.004)
Vcc = ufloat(19.85, 0.11)
R1 = ufloat(177.1e3, 1.5e3)
R2 = ufloat(18.06e3, 0.15e3)
Re = ufloat(986, 9)
Rc = ufloat(9.93e3,0.09e3)
hfe = ufloat(130.1,2.2)
Vcm = ufloat(9.28, 0.06)
Vbm = ufloat(1.692, 0.009)
Vem = ufloat(1.070, 0.006)
Icm = ufloat(1.058e-3, 0.009e-3)
Vcem = ufloat(8.21, 0.05)

# formule per calcolare le cose attese

Vbb = Vcc*R2/(R1 + R2)
Rb = R1*R2/(R1 + R2)
Ib = (Vbb - Vbe)/(Re*(hfe + 1) + Rb)
Ic = hfe*Ib
Ie = Ic + Ib
Vb = Vbe + Re*(hfe + 1)*Ib
Ve = Vb - Vbe
Vc = Vcc - Ic*Rc
Vce = Vc - Ve

# compatibilità

DVc = Vcm - Vc
DVb = Vbm - Vb
DVe = Vem -Ve
DVce = Vcem -Vce
DIc = Icm -Ic
