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

file="loopgain1"

def f(x, a, b):
#    return log10(a*(1/(1+(b/(10**x))**2)*1/(1+((10**x)/c)**2))**0.5)
#    return b/np.sqrt(1+(a/x)**2)*1/np.sqrt(1+(x/a)**2)*1/(1+(1/np.sqrt(1+(a/x)**2)*1/np.sqrt(1+(x/a)**2)))
    return b*((x/a)**2/((1-(x/a)**2)**2+(3*x/a)**2))**0.5

p0=[1550,3]

def XYfun(a):
#    return unumpy.log10(a[0]), 20*unumpy.log10(a[1]/a[3])
    return a[0], a[1]/a[3]

unit = [("freq", "osc"),("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

titolo = "Loop gain"
Xlab = "freq. [Hz]"
Ylab = "gain"

tab = ["frequency [Hz]", "$V_A$ [V]", "$\\varphi$ [s]", "$V_A$ [V]"]

#fit(dir, file, unit, f, p0, titolo, Xlab, Ylab, XYfun, Xscale="log", Yscale="log", out=False)
###########################################################################

#LOOP GAIN MODULI_plot#

file="loopgain1"
fig="loopgain_modulo"
def XYfun(a):
    return unumpy.log10(a[0]), 20*unumpy.log10(a[1]/a[3])

unit = [("freq", "osc"),("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

data = load_data(dir,file)
X, Y, dX, dY, data_err = errors(data, unit, XYfun)

def f(x, a, b):
#    return log10(a*(1/(1+(b/(10**x))**2)*1/(1+((10**x)/c)**2))**0.5)
#    return b/np.sqrt(1+(a/x)**2)*1/np.sqrt(1+(x/a)**2)*1/(1+(1/np.sqrt(1+(a/x)**2)*1/np.sqrt(1+(x/a)**2)))
    return 20*log10(b*((10**x/a)**2/((1-(10**x/a)**2)**2+(3*10**x/a)**2))**0.5)

p0=[1597,2.953]

titolo = "Bode plot - modulo"
Xlab = "Frequenza [decadi]"
Ylab = "Gaudagno [dB]"
xlimp = [99.5, 101]

#plot_fit(dir, file, titolo, unit, f, p0, X, Y, dX, dY, fig=fig, xlimp=xlimp, XYfun=XYfun, Xlab=Xlab, Ylab=Ylab)
###########################################################################

#LOOP GAIN FASI#

file = "loopgain"


def f(x, a):
    return arctan((1-(x/a)**2)/(3*x/a))
p0=[1500]

def XYfun(a):
    return a[0], a[2]*a[0]*2*pi

unit = [("freq", "osc"), ("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

titolo = "Bode plot - fasi"
Xlab = "Frequenza [decadi]"
Ylab = "Fase [rad]]"

tab = ["frequency [Hz]", "$V_A$ [V]", "$\\varphi$ [s]", "$V_A$ [V]"]

fit(dir, file, unit, f, p0, titolo, Xlab, Ylab, XYfun, Xscale="log",  out=True)
###########################################################################


#LOOP GAIN MODULI_plot#

file="loopgain"
fig="loopgain_fase"
def XYfun(a):
    return unumpy.log10(a[0]), a[2]*a[0]*2*pi

unit = [("freq", "osc"),("volt_nc", "osc"), ("time", "osc"), ("volt_nc", "osc")]

data = load_data(dir,file)
X, Y, dX, dY, data_err = errors(data, unit, XYfun)

def f(x, a):
    return arctan((1-(10**x/a)**2)/(3*10**x/a))

p0=[1856]

titolo = "Bode plot - fasi"
Xlab = "Frequenza [decadi]"
Ylab = "Fase [rad]"
xlimp = [99.5, 101]

plot_fit(dir, file, titolo, unit, f, p0, X, Y, dX, dY, fig=fig, xlimp=xlimp, XYfun=XYfun, Xlab=Xlab, Ylab=Ylab, out=True)