from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione2/"

###########################################################################

#PASSA BASSO DA DIMENSIONARE#

file="Bode_Lowpass_800ohm"

def f(x, a):
    return 1/sqrt(1+(x/a)**2)

p0=[200]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode - passa basso"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [$V$]","Tensione in uscita [$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

#PASSA BASSO RETTA 1#

file="retta_lowpass_1"
fig="rette"
def f(x, a,b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20* unumpy.log10(a[2]/a[1])

unit=["tempo_osc","volt_osc","volt_osc"]


titolo="Passa basso - fit lineare"
Xlab="Frequenza [decadi]"
Ylab="Ampiezza [dB]"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita [V]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=fig,xlimp=[80,130])

###########################################################################

#PASSA BASSO RETTA 2#

file="retta_lowpass_2"
fig="rette"
def f(x, a,b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20*unumpy.log10(a[2]/a[1])

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Passa basso - fit lineare"
Xlab="Frequenza [decadi]"
Ylab="Ampiezza [dB]"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita [V]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=fig,xlimp=[80,105])

###########################################################################

#PASSA BASSO FAST#

file="Fast_fit_lowpass"

def f(x, a):
    return 1/sqrt(1+(x/a)**2)

p0=[5000]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode - passa basso"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita [V]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

#PASSA ALTO FAST#

file="Fast_fit_highpass"

def f(x, a):
    return 1/sqrt(1+(a/x)**2)

p0=[500]

def XYfun(a):
    return a[0], a[2]/a[1]

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Diagramma di Bode - passa alto"
Xlab="Frequenza [Hz]"
Ylab="Ampiezza"

tab=["Frequenza [Hz]","Tensione in ingresso [V]","Tensione in uscita [V]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

#PASSA BANDA#

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

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,table=True,Xscale="log",Yscale="log",tab=tab)

###########################################################################

#PASSA BANDA RETTA 1#

file="passabandar1"
figura="passabandar"

def f(x, a,b):
    return a*x + b

p0 = [1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20 * unumpy.log10(a[2]/a[1])

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Passa banda - fit lineare"
Xlab="Frequenza [decadi]"
Ylab="Ampiezza [dB]"

xlimp1=array([90.,115.])


fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=figura,xlimp=xlimp1)

###########################################################################

#PASSA BANDA RETTA 2#

file="passabandar2"
figura="passabandar"

def f(x, a,b):
    return a*x + b

p0 = [1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20*unumpy.log10(a[2]/a[1])

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Passa banda - fit lineare"
Xlab="Frequenza [decadi]"
Ylab="Ampiezza [dB]"

xlimp2=array([80.,110.])


fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=figura,xlimp=xlimp2)

###########################################################################

#PASSA BANDA RETTA 3#

file="passabandar3"
figura="passabandar"

def f(x, a,b):
    return a*x + b

p0 = [1,1]

def XYfun(a):
    return unumpy.log10(a[0]), 20 * unumpy.log10(a[2]/a[1])

unit=["tempo_osc","volt_osc","volt_osc"]

titolo="Passa banda - fit lineare"
Xlab="Frequenza [decadi]"
Ylab="Ampiezza [dB]"

xlimp3=array([95.,105.])


fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,fig=figura, xlimp=xlimp3)
