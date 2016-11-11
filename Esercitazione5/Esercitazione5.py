from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione5\\"
###########################################################################

file="nomesensato"

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere"]

titolo="ciaociao"
Xlab=""
Ylab=""

tab=["",""]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab)

###########################################################################

#GUADAGNO VS TENSIONE#

file="guadagnovstensione"

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt_osc_nocal","volt_osc_nocal"]

titolo="$V_{OUT}$ vs $V_{IN}$"
Xlab="Tensione in ingresso $V_{IN}$ [$V$]"
Ylab="Tensione in uscita $V_{OUT}$ [$V$]"

tab=["$V_{IN}$","$V_{OUT}$"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################