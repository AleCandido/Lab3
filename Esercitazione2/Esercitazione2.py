from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
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

dir= path + "Esercitazione2\\"
file="Fast_fit_lowpass"

def f(x, a):
    return 1/sqrt(1+(x/a)**2)

p0=[5000]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,scarti=True,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

dir= path + "Esercitazione2\\"
file="Fast_fit_highpass"

def f(x, a):
    return 1/sqrt(1+(a/x)**2)

p0=[500]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,scarti=True,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

dir= path + "Esercitazione2\\"
file="passabanda"

def f(x, a,b,c):
    return 1/sqrt(1+(a/x)**2)*1/sqrt(1+(x/b)**2)*1/(1+c*(1/sqrt(1+(a/x)**2)*1/sqrt(1+(x/b)**2)))

p0=[500,5000,1]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,scarti=True,table=True,Xscale="log",Yscale="log",tab=tab)