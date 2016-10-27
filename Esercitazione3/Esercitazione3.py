from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione3/"
###########################################################################

#V_EARLY#

file="Early"
R = uncertainties.ufloat(989,mme(989,"ohm"))
def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[1],(a[0]-a[1])*10e3/R

unit=["volt","volt"]

titolo="$I_C$ vs $V_{CE}$"
Xlab="Tensione collettore/emettitore $V_{CE}$ [$V$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"

tab=["$V_1$","$V_{CE}$"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab)

###########################################################################

#V_EARLY1#

file="Early1r"
fig="Earlyr"
R = uncertainties.ufloat(989,mme(989,"ohm"))
def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[1],(a[0]-a[1])*10e3/R

unit=["volt","volt"]

titolo="$I_C$ vs $V_{CE}$"
Xlab="Tensione collettore/emettitore $V_{CE}$ [$V$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"
tab=["$V_1$","$V_{CE}$"]
xlimp=[80,150]
fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,fig=fig,xlimp=xlimp)

###########################################################################

#V_EARLY2#

file="Early2r"
fig="Earlyr"
R = uncertainties.ufloat(989,mme(989,"ohm"))
def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[1],(a[0]-a[1])*10e3/R

unit=["volt","volt"]

titolo="$I_C$ vs $V_{CE}$"
Xlab="Tensione collettore/emettitore $V_{CE}$ [$V$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"

tab=["$V_1$","$V_{CE}$"]
xlimp=[60,120]
fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,table=True,tab=tab,fig=fig,xlimp=xlimp)

###########################################################################

#FAST PLOT I_C VS I_B#

file="ib_var"
fig="Ic_Ib"
RL = uncertainties.ufloat(989,mme(989,"ohm"))
RB = uncertainties.ufloat(46.4e3,mme(46.4e3,"ohm"))
V1 = uncertainties.ufloat(9.84,mme(9.84,"volt"))
V2 = uncertainties.ufloat(5.2,5.2*0.03)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[0]/RB*10**6,(V1-a[2])/RL*10**3

unit=["volt","volt_osc","volt_osc"]

titolo="$I_c$ vs $I_b$"
Xlab="Corrente di base $I_B$ [$\mu A$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"

tab=["$V_{RB}$ [$V$]","$V_{BE}$ [$V$]","$V_{CE}$[$V$]"]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,fig=fig,table=True, tab=tab)

###########################################################################

#H_FE FIT#

file="h_fe"
RL = uncertainties.ufloat(989,mme(989,"ohm"))
RB = uncertainties.ufloat(46.4e3,mme(46.4e3,"ohm"))
V1 = uncertainties.ufloat(9.84,mme(9.84,"volt"))
V2 = uncertainties.ufloat(5.2,5.2*0.03)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[0]/RB*10**6,(V1-a[2])/RL*10**3

unit=["volt","volt_osc","volt_osc"]

titolo="$I_c$ vs $I_b$"
Xlab="Corrente di base $I_B$ [$\mu A$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True)

###########################################################################

#FAST PLOT I_C VS V_BE#

file="ib_var"
fig="Ic_Vbe"
R1 = uncertainties.ufloat(989,mme(989,"ohm"))
RB = uncertainties.ufloat(46.4e3,mme(46.4e3,"ohm"))
V1 = uncertainties.ufloat(9.84,mme(9.84,"volt"))
V2 = uncertainties.ufloat(5.2,5.2*0.03)

def f(x, a, b):
    return a*x+b

p0=[1,1]

def XYfun(a):
    return a[1]*10**3,(V1-a[2])/RL*10**3

unit=["volt","volt_osc","volt_osc"]

titolo="$I_c$ vs $V_{BE}$"
Xlab="Corrente di base $I_B$ [$\mu A$]"
Ylab="Corrente di collettore $I_C$ [m$A$]"

tab=["",""]

fit(dir,file,unit,f,p0,titolo,Xlab,Ylab,XYfun,preplot=True,fig=fig)

###########################################################################
