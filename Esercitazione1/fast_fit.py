from pylab import *

###########################################################################

dir= "C:\\Users\\Roberto\\Desktop\\Ale_Bob\\Esercitazione1\\"
file=   "1KOhm"

def f(x, a, b): #funzione da fittare
    return a+b*x

p0=[1,1] #parametri iniziali

xunit="volt"
yunit="volt"

titolo="Grafico $V_{in}$ vs $V_{out}$ per resistenze $\sim 1 K \Omega$"
Xlab="Tensione $V_{in}$ [$V$]"
Ylab="Tensione $V_{out}$ [$V$]"

fit(dir,file,xunit,yunit,f,p0,titolo,Xlab,Ylab,table="true")

##########################################################################

directory="C:\\Users\\Roberto\\Desktop\\Ale_Bob\\Esercitazione1\\"
file="4MOhm"

def f(x, a, b): #funzione da fittare
    return a+b*x

p0=[1,1] #parametri iniziali

xunit="volt"
yunit="volt"

titolo="Grafico $V_{in}$ vs $V_{out}$ per resistenze $\sim 4 M \Omega$"
Xlab="Tensione $V_{in}$ [$V$]"
Ylab="Tensione $V_{out}$ [$V$]"

fit(directory,file,xunit,yunit,f,p0,titolo,Xlab,Ylab,table="true")