import getpass
import sys
from uncertainties import unumpy
import numpy as np

if getpass.getuser() == "alessandro":
    path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
elif getpass.getuser() == "Roberto":
    path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
elif getpass.getuser() == "Studenti":
    path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
else:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")
sys.path = sys.path + [path]

from BobLightyear import *

dir= path + "Esercitazione8/"
###########################################################################

#LOOP GAIN MODULI#

file="loopgain"

def f(x, a, b):
    return a*x +b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20*unumpy.log10(a[1]/a[3] )

unit = [("freq", "osc"),("volt", "osc"), ("time", "osc"), ("volt", "osc")]

titolo = "Loop gain - Bode plot"
Xlab = "freq. [decades]"
Ylab = "gain [dB]"

tab = ["frequency [Hz]", "$V_A$ [V]", "$\\varphi$", "$V_A$ [V]"]

fit(dir, file, unit, f, p0, titolo, Xlab, Ylab, XYfun, table=True, tab=tab, out=False)
###########################################################################

