import getpass
import sys
from uncertainties import unumpy
import numpy as np

if getpass.getuser() == "alessandro":
    path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
elif getpass.getuser() == "Roberto":
    path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
elif getpass.getuser() == "Studenti":
    path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
else:
    raise Error("unknown user, please specify it and the path in the file Esercitazione*.py")
sys.path = sys.path + [path]

from BobLightyear import *

dir= path + "Esercitazione8/"
###########################################################################

#GRAFICO GAIN-BANDWIDTH#

file=""

def f(x, ):
    return 

p0=[1,1]

def XYfun(a):
    return , 

unit=[(),()]

titolo=
Xlab=
Ylab=

tab=[]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun, table=True, tab=tab, out=True)
###########################################################################

