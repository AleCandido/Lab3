from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione6/"
###########################################################################

#GUADAGNO AMPLIFICATORE INVERTENTE#

file="inv_amp_gain"

def f(x, a, b):
    return a+b*x

p0=[0,10]

def XYfun(a):
    return a[0],a[1]

unit=["volt_osc_nocal","volt_osc_nocal"]

titolo="$V_{OUT}$ vs $V_{IN}$"
Xlab="Tensione di input $V_{IN}$ [$V$]"
Ylab="Tensione di output $V_{OUT}$ [$V$]"

tab=["$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab)

###########################################################################

#DIAGRAMMA DI BODE AMPLIFICATORE INVERTENTE#

file="inv_amp_f_domain"

VIN = uncertainties.ufloat(496e-3, 496e-3*0.035)

def f(x, a ,b):
    return a/(1+(x/b)**2)**0.5

p0=[9.8,1.9*1e5]

def XYfun(a):
    return a[0],a[1]/VIN

unit=["tempo_osc","volt_osc"]

titolo="Diagramma di bode - amplificatore invertente"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]
xlimp=[100,110]
fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log",xlimp=xlimp)

###########################################################################

#40 Db ??#

file="30db"
fig="rette"
VIN = uncertainties.ufloat(496e-3, 496e-3*0.025)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]),20*unumpy.log10(a[1]/VIN)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [decadi]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,xlimp=[98,101],fig=fig)

###########################################################################

#20 Db ??#

file="20db"
fig="rette"
VIN = uncertainties.ufloat(496e-3, 496e-3*0.025)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]),20*unumpy.log10(a[1]/VIN)

unit=["tempo_osc","volt_osc_nocal"]

titolo="Diagramma di Bode"
Xlab="Frequenza [decadi]"
Ylab="Guadagno $A_v$ [dB]"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,xlimp=[99,102],fig=fig)

###########################################################################

#GRAFICO GAIN-BANDWIDTH#

file="gain_bandwidth"

VIN2 = uncertainties.ufloat(42.4e-3, 42.4e-3*0.025)

def f(x, a,b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[1]),20*unumpy.log10(a[0]/VIN2)

unit=["volt_osc_nocal","volt_osc"]

titolo="Grafico gain-bandwidth"
Xlab="Frequenza di taglio [decadi]"
Ylab="Guadagno [dB]"

tab=["$V_{OUT}$ [$V$]","Freq. di taglio [Hz]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True,tab=tab)
a = uncertainties.ufloat(-20.49 , 0.21)
b = uncertainties.ufloat(128.8 , 0.9)
#print ("Prodotto gain-bandwidth =", 10**(-b/a))
###########################################################################

#INTEGRATORE MODULO#

file="low_pass"
fig = "module_low_pass"
def f(x, a , b):
    return a*1/(1+(x/b)**2)**0.5

p0=[10,352]

def XYfun(a):
    return a[0],a[2]/a[3]

unit=["tempo_osc","volt_osc_nocal","volt_osc","volt_osc"]

titolo="Diagramma di bode - integratore"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","Sfasamento [s]","$V_{OUT}$ [$V$]","$V_{IN}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log",fig=fig)

###########################################################################

#INTEGRATORE FASE#

file="low_pass"
fig = "phase_low_pass"
def f(x, a):
    return arctan(x/a)


p0=[404]

def XYfun(a):
    return a[0], 2*pi*(a[1]*a[0]-0.5)

unit=["tempo_osc","volt_osc_nocal","volt_osc","volt_osc"]

titolo="Diagramma di bode - integratore"
Xlab="Frequenza [Hz]"
Ylab="Fase [rad]"

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, Xscale="log",fig=fig)

###########################################################################

#DERIVATORE MODULO#

file="high_pass"
fig="module_high_pass"
def f(x, a, b, c):
    return a*(1/(1+(b/x)**2)*1/(1+(x/c)**2))**0.5

p0=[10,3.56e+03,2e+05]

def XYfun(a):
    return a[0],a[2]/a[1]

unit=["tempo_osc","volt_osc_nocal","volt_osc_nocal","volt_osc_nocal"]

titolo="Diagramma di bode - derivatore"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]","Sfasamento [s]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log",fig=fig)

###########################################################################

#DERIVATORE FASE#

file="high_pass_phase"
fig="phase_high_pass"
def f(x, a, b):
    return (-arctan(a/x)-arctan(b/x)+pi/2)

p0=[3.56e+03, 2e+05]

def XYfun(a):
    return a[0], 2*pi*(a[3]*a[0]-1/2)

unit=["tempo_osc","volt_osc","volt_osc","volt_osc_nocal"]

titolo="Diagramma di bode - derivatore"
Xlab="Frequenza [Hz]"
Ylab="Fase [rad]"

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, Xscale="log", fig=fig)

###########################################################################
