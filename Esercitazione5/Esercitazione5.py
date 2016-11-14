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

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun)

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

tab=["$V_{IN} [$V$]$","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

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

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

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

tab=["$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

#GUADAGNO VS Id#

file="guadagnovsid"

VIN=uncertainties.ufloat(740e-3,740e-3*0.025)
RS = uncertainties.ufloat(244 , 3)
RD = uncertainties.ufloat(985, 9)

def f(x, a, b): 
    return a/b*(1-1/(1+b*x**0.5))

p0=[1,1]

def XYfun(a):
    return a[1],a[0]/VIN

unit=["volt_osc_nocal","ampere"]

titolo="$V_{OUT}$ vs $V_{IN}$"
Xlab="Corrente di Drain $I_D$ [$A$]"
Ylab="Guadagno $|A_v|$"

tab=["$V_{IN}$","$I_D$"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

file="carattx"

def f(x, a,x0):
    return a*(x-x0)
    
p0=[1,1]

unit=["volt","ampere_anal"]

titolo=""
Xlab="$V_{GS}$~[$V$]"
Ylab="$I_D$~[$A$]"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,tab=tab)

###########################################################################

file="carattx2"

def f(x, a, x0):
    return a*(x - x0)**2/1000

p0=[1,1]

def XYfun(a):
    return -a[0],a[1]/1000

unit=["volt","ampere_anal"]

titolo="Curva caratteristica di gate del JFET"
Xlab="Tensione Gate-SOurce $V_{GS}$ [$V$]"
Ylab="Corrente di Drain $I_D$ [$mA$]"
xlimp=[101,99]
tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,tab=tab,xlimp=xlimp)

###########################################################################


file="caratterizzazioneJFET"

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return -a[0],a[1]

unit=["volt","ampere"]

titolo="Curva caratteristica di gate del JFET"
Xlab="$Tensione Gate-Source V_{GS} [$V$]$"
Ylab="$Corrente di Drain I_D [$A$]$"

tab=["-$V_{GS}$ [$V$]","$I_D$ [$A$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,scarti=True,tab=tab, table=True)

###########################################################################
