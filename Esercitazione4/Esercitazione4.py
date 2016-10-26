from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione4\\"
###########################################################################

#FREQUENCY DOMAIN#

file="f_domain"
V1 = uncertainties.ufloat(1.00,1.00*0.035)

def f(x, a, b, c):
    return c/sqrt(1+(a/x)**2)*1/sqrt(1+(x/b)**2)

p0=[1,1,1]

def XYfun(a):
    return a[0],a[1]/V1

unit=["tempo_osc","volt_osc"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Guadagno $A_v$"

tab=["Frequenza [Hz]","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,Xscale="log",Yscale="log")

###########################################################################

#GUADAGNO CON C_E#

file="C_E"

def f(x, a):
    return 0*x + a

p0=[40]

def XYfun(a):
    return a[0],a[1]/a[0]

unit=["volt_osc","volt_osc"]

titolo="Guadagno con condensatore $C_E$"
Xlab="Tensione di ingresso $V_{IN}$ [$V$]"
Ylab="Guadagno $A_v$"

tab=["$V_{IN} [$V$]$","$V_{OUT}$ [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab)

###########################################################################