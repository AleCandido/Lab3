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
from pylab import log10, arctan, pi

dir= path + "Esercitazione8/"
###########################################################################

#LOOP GAIN MODULI#

file="loopgain"

def f(x, a, b, c):
#    return log10(a*(1/(1+(b/(10**x))**2)*1/(1+((10**x)/c)**2))**0.5)
    return a*(1/(1+(b/x)**2)*1/(1+(x/c)**2))**0.5

p0=[7.8,4.20e3,607]

def XYfun(a):
#    return unumpy.log10(a[0]), 20*unumpy.log10(a[1]/a[3])
    return a[0], a[1]/a[3]

unit = [("freq", "osc"),("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

titolo = "Loop gain"
Xlab = "freq. [Hz]"
Ylab = "gain"
xlimp = [90, 110]

tab = ["frequency [Hz]", "$V_A$ [V]", "$\\varphi$ [s]", "$V_A$ [V]"]

fit(dir, file, unit, f, p0, titolo, Xlab, Ylab, XYfun, table=True, tab=tab, out=False, xlimp=xlimp)
###########################################################################

#LOOP GAIN MODULI_plot#

file="loopgain"

fig = "loopgain_bode"

def XYfun(a):
    return unumpy.log10(a[0]), 20*unumpy.log10(a[1]/a[3])

unit = [("freq", "osc"),("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

data = load_data(dir,file)
X, Y, dX, dY, data_err = errors(data, unit, XYfun)

def f(x, a, b, c):
    return 20*log10(a*(1/(1+(b/(10**x))**2)*1/(1+((10**x)/c)**2))**0.5)

p0=[1.126,607,4.2e3]

titolo = "Loop gain - Bode plot"
Xlab = "freq. [decades]"
Ylab = "gain [dB]"
xlimp = [99.5, 101]

plot_fit(dir, file, titolo, unit, f, p0, X, Y, dX, dY, fig=fig, xlimp=xlimp, XYfun=XYfun, Xlab=Xlab, Ylab=Ylab)
###########################################################################

#LOOP GAIN FASI#

file = "loopgain"

fig = "loopgain_ph"

def f(x, a, b, c):
    return c*(arctan(a/x) - arctan(x/b))/pi

p0=[607, 4.20e3, 1]

def XYfun(a):
    return a[0], a[2]*a[0]

unit = [("freq", "osc"), ("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]
# c'è un arbitrario 5% di errore su time osc in BobLightyear
#in realtà un bel po' di errore c'era per davvero a causa del rumore

titolo = "Loop gain, fasi"
Xlab = "freq. [Hz]"
Ylab = "phase [$\pi$ rad]"
xlimp = [99, 102]

fit(dir, file, unit, f, p0, titolo, Xlab, Ylab, XYfun, residuals=True, xlimp=xlimp, fig=fig, Xscale="log")
###########################################################################
