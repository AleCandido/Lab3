from pylab import *
sys.path = sys.path +["C:\\Users\\Roberto\\Documents\\GitHub\\Lab3"]
from analizer import *
###########################################################################

dir=""
file=""

def f(x, a, b): #funzione da fittare
    return a+b*x

p0=[1,1]

def Xfun(a,b): #formula per il calcolo della X dalle colonne (a,b) del file in input
    return a
def Yfun(a,b): #idem per la Y
    return b
    
def Xerr(a,b,a_err,b_err): #propagazione errore sulle X
    return a_err
def Yerr(a,b,a_err,b_err): #propagazione errore sulle Y
    return b_err

xunit=""
yunit=""

titolo=""
Xlab=""
Ylab=""

fit(dir,file,xunit,yunit,f,p0,titolo,Xlab,Ylab,Xfun,Yfun,Xerr,Yerr,preplot=True,scarti=True,tabella=True)

###########################################################################

