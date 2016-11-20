from pylab import *

import sys
if sys.argv[0] == ale
    path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
elif sys.argv[0] == lab
    path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
else
    path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
sys.path = sys.path + [path]
dir= path + "Esercitazione/"

from analyzer import *
import uncertainties
###########################################################################

file=""

def f(x, a, b):
    return a+b*x

p0=[1,1]

def XYfun(a):
    return a[0],a[1]

unit=[("",""),("","")]

titolo=""
Xlab=""
Ylab=""

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun)

###########################################################################