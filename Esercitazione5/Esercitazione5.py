from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione5/"
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

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun)

###########################################################################

#LINEARITA'#

file="linearity"

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

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

#GUADAGNO VS TENSIONE2#

file="guadagnovstensione2"

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

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

#LINEARITA' 2#

file="linearity2"

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

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

file="carattx"

def f(x, a,x0):
    return a*(x-x0)
    
p0=[1,1]

unit=["volt","ampere_anal"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,tab=tab)

###########################################################################

file="carattx2"

def f(x, a, x0):
    return a*(x - x0)**2

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere_anal"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"
xlimp=[99,101]
tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,tab=tab,xlimp=xlimp)

###########################################################################


file="caratterizzazioneJFET"

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt","ampere_anal"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$V_{GS}$"
Ylab="$I_D$"

tab=["",""]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab)

###########################################################################