from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione4/"

###########################################################################

#GUADAGNO per piccoli segnali#

file="guadagnopiccolisegnali"

def f(x, a, b):
    return a*x + b

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt_osc_nocal","volt_osc_nocal"]

titolo="Guadagno dell'amplificatore per piccoli segnali"
Xlab="Tensione di ingresso $V_{IN}$ [$V$]"
Ylab="Tensione di uscita $V_{OUT}$ [$V$]"

tab=["$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,scarti=True)

###########################################################################

#GUADAGNO per piccoli segnali outlier#

file="guadagnopiccolisegnali_ol"

def f(x, a, b):
    return a*x + b

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt_osc_nocal","volt_osc_nocal"]

titolo="Guadagno dell'amplificatore per piccoli segnali"
Xlab="Tensione di ingresso $V_{IN}$ [$V$]"
Ylab="Tensione di uscita $V_{OUT}$ [$V$]"

tab=["$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,scarti=True)

###########################################################################

#FREQUENCY DOMAIN _ plot#

file="f_domain"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b, c):
    return c/sqrt(1+(a/x)**2)*1/sqrt(1+(x/b)**2)

p0=[1,1,1]

def XYfun(a):
    return a[0],20*unumpy.log10(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,Xscale="log")

###########################################################################

#FREQUENCY DOMAIN _ low_frequency #

file="low_frequency"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b):
    return b/sqrt(1+(a/x)**2)

p0=[48,1]

def XYfun(a):
    return a[0],(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Guadagno $A_v$"

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,Yscale="log",Xscale="log")

###########################################################################

#FREQUENCY DOMAIN _ high_frequency #

file="high_frequency"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b):
    return b/sqrt(1+(x/a)**2)

p0=[1,1]

def XYfun(a):
    return a[0],(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Guadagno $A_v$"

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,Yscale="log",Xscale="log")

###########################################################################

#FREQUENCY DOMAIN - retta 1#

file="f_domain_retta1"
fig="f_domain_rette"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]),20*unumpy.log10(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [decadi]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=fig,xlimp=[80,120])

###########################################################################


#FREQUENCY DOMAIN - retta 2#

file="f_domain_retta2"
fig="f_domain_rette"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]),20*unumpy.log10(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [decadi]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=fig,xlimp=[70,120])

###########################################################################


#FREQUENCY DOMAIN - retta 3#

file="f_domain_retta3"
fig="f_domain_rette"
V1 = uncertainties.ufloat(1.00,1.00*0.015)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]),20*unumpy.log10(a[1]/V1)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [decadi]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=fig,xlimp=[92,102])

###########################################################################

#GUADAGNO CON C_E#

file="C_E"

def f(x, a, b):
    return a*x + b

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["volt_osc_nocal","volt_osc_nocal"]

titolo="Guadagno con condensatore $C_E$"
Xlab="Tensione di ingresso $V_{IN}$ [$V$]"
Ylab="Guadagno $A_v$"

tab=["$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab)

###########################################################################
