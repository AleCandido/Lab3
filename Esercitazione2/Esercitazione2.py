from pylab import *
sys.path = sys.path +["C:\\Users\\Roberto\\Documents\\GitHub\\Lab3"]
from analyzer import *
###########################################################################

dir="C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\Esercitazione2\\"
file="Bode_Lowpass_800ohm"

def f(x, a):
    return 1/sqrt(1+(x/a)**2)

p0=[200]

def Xfun(a):
    return a[0]
def Yfun(a):
    return a[2]/a[1]
    
def Xerr(a,a_err):
    return a_err[0]
def Yerr(a,a_err):
    return (a[2]/a[1])*0.02

unit=["volt","volt","volt"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,Xfun,Yfun,Xerr,Yerr,preplot=True,scarti=True,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

