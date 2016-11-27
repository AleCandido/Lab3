import getpass
import sys
from uncertainties import unumpy

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
    return unumpy.log10(a[1]), 20*unumpy.log10(a[0]/VIN2)

unit=[("volt_ar","osc"),("freq","osc")]

titolo="Grafico gain-bandwidth"
Xlab="Frequenza [decadi]"
Ylab="Guadagno [dB]"

tab=["$V_{OUT}$ [$V$]","Freq. [Hz]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True, tab=tab, out=True)
#(a,b)=uncertainties.correlated_values_norm([(-19.5 , 0.7),(125 , 4)],  [[ 1. ,-0.99871014],[-0.99871014, 1. ]])
#print ("Prodotto gain-bandwidth =", 10**(-b/a))
###########################################################################

##

file="V_t"
def f(x, a, b):
    return a*np.log(x/b)

p0=[1,1]

def XYfun(a):
    return a[0], a[1]

unit=[("volt_nc","osc"),("time","osc")]

titolo="Grafico gain-bandwidth"
Xlab="Tensione in ingresso [$V$]"
Ylab="Durata segnale in uscita [s]"

tab=["$V_{IN}$ [$V$]","TOT [s]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True, tab=tab)

###########################################################################