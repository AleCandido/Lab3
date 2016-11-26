import getpass
import sys
from uncertainties import unumpy as u
from uncertainties import *
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

dir= path + "Esercitazione7/"
###########################################################################

#GRAFICO GAIN-BANDWIDTH#

file="gain_bandwidth"

def f(x, a, b):
    return a+b*x

VIN2 = umme(156e-3,"volt_ar","osc")

p0=[1,1]

def XYfun(a):
    return u.log10(a[1]), u.log10(a[0]/VIN2)

unit=[("volt_ar","osc"),("freq","osc")]

titolo="Grafico gain-bandwidth"
Xlab="Frequenza di taglio [decadi]"
Ylab="Guadagno [dB]"

tab=["$V_{OUT}$ [$V$]","Freq. di taglio [Hz]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True, tab=tab, out=True)

###########################################################################

##

file="V_t"
def f(x, a, b):
    return a*np.log10(x*b)

p0=[1,1]

def XYfun(a):
    return a[0], a[1]

unit=[("volt_ar_nc","osc"),("time","osc")]

titolo="Grafico gain-bandwidth"
Xlab="Tensione di soglia"
Ylab="Tempo"

tab=["$V_{OUT}$ [$V$]","Freq. di taglio [Hz]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True, tab=tab, residuals=True)

###########################################################################