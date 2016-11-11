from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione5/"
###########################################################################

file="caratterizzazioneJFET"

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab)

###########################################################################

file="carattx"

def f(x, a, x0):
    return a*(x-x0)

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab)

###########################################################################

file="carattx2"

def f(x, a, b, x0):
    return a*(x - x0)**2 + b

p0=[1,1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab)

###########################################################################
