from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione6\\"
###########################################################################

#GUADAGNO AMPLIFICATORE INVERTENTE#

file="inv_amp_gain"

def f(x, a, b):
    return a+b*x

p0=[1,1]

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
    return a*1/(1+(x/b)**2)

p0=[1,1]

def XYfun(a):
    return a[0],a[1]/VIN

unit=["tempo_osc","volt_osc"]

titolo="Diagramma di bode - amplificatore invertente"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log")

###########################################################################

#GRAFICO GAIN-BANDWIDTH#

file="gain_bandwidth"

VIN2 = uncertainties.ufloat(42.4e-3, 42.4e-3*0.035)

def f(x, a):
    return a/x

p0=[1]

def XYfun(a):
    return a[0]/VIN2,a[1]

unit=["volt_osc","volt_osc"]

titolo="Grafico gain-bandwidth"
Xlab="Guadagno"
Ylab="Frequenza di taglio [Hz]"

tab=["$V_{OUT}$ [$V$]","Freq. di taglio [Hz]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,scarti=True,table=True,tab=tab)

###########################################################################

#PASSA BASSO MODULO#

file="low_pass"
fig = "module_low_pass"
def f(x, a , b, c):
    return a*1/(1+(x/b)**c)

p0=[1,1,1]

def XYfun(a):
    return a[0],a[2]/a[3]

unit=["tempo_osc","tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di bode - passa basso"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","Sfasamento [s]","$V_{OUT}$ [$V$]","$V_{IN}$ [$V$]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log",fig=fig)

###########################################################################

#PASSA BASSO FASE#

file="low_pass"
fig = "phase_low_pass"
def f(x, a,b):
    return arctan(a*x)+b

p0=[1,1]

def XYfun(a):
    return a[0],pi*a[1]*a[0]

unit=["tempo_osc","tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di bode - passa basso"
Xlab="Frequenza [Hz]"
Ylab="Fase [rad]"

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True, Xscale="log",fig=fig)

###########################################################################

#PASSA ALTO MODULO#

file="high_pass"
fig="module_high_pass"
def f(x, a, b, c, d, e):
    return a*1/(1+(b/x)**d)*1/(1+(x/c)**e)

p0=[10,2e2,2e5,2,2]

def XYfun(a):
    return a[0],a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc","tempo_osc"]

titolo="Diagramma di bode - passa alto"
Xlab="Frequenza [Hz]"
Ylab="Guadagno"

tab=["Frequenza [Hz]","$V_{IN}$ [$V$]","$V_{OUT}$ [$V$]","Sfasamento [s]"]

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,tab=tab, Xscale="log",Yscale="log",fig=fig)

###########################################################################

#PASSA ALTO FASE#

file="high_pass"
fig="phase_high_pass"
def f(x, a,b):
    return arctan(a*x)+b

p0=[1,1]

def XYfun(a):
    return a[0],a[3]*a[0]

unit=["tempo_osc","volt_osc","volt_osc","tempo_osc"]

titolo="Diagramma di bode - passa alto"
Xlab="Frequenza [Hz]"
Ylab="Fase [rad]"

#fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, preplot = True, Xscale="log",fig=fig)

###########################################################################