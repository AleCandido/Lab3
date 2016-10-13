from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
sys.path = sys.path + [path]
from analyzer import *
###########################################################################

dir=path+""
file=""

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=["",""]

titolo=""
Xlab=""
Ylab=""

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot="true",scarti="true",tabella="true",tab=tab)

###########################################################################

