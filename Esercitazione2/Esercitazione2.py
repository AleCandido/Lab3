from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
sys.path = sys.path + [path]
from analyzer import *
###########################################################################

dir= path + "Esercitazione2\\"
file="Bode_Lowpass_800ohm"

def f(x, a):
    return 1/sqrt(1+(x/a)**2)

p0=[200]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,scarti=True,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

