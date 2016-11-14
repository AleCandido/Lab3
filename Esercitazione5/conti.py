from analyzer import *
from uncertainties import *

gm = ufloat(3.98e-3, 0.06e-3)
RS = ufloat(244 , 2.8)
RD = ufloat(985, 9)
f1 = ufloat(1011,1011*0.01)
f10 = ufloat(10040,10040*0.01)
A1 = gm*RD/(1+gm*RS)
A2 = gm*RS/(1+gm*RS)

#print (A1,"\n",A2)

VIN=ufloat(740e-3,20e-3)
VOUT=ufloat(3.60,0.09)

A=VOUT/VIN

#print(A)

RO = ufloat(1e6,0.02e6)
RG = ufloat(4.65e6,mme(4.65e6,"ohm"))
#RIN=((1/RO)+(1/RG))**(-1.)

#print(RIN)

V1=ufloat(2.80,2.80*0.035)
V2=ufloat(1.42,1.42*0.035)
R=ufloat(677e3,mme(677,"ohm"))

REQ=(V2/(V1-V2))*R

print(REQ)

RIN1k = REQ*RO/(RO-REQ)
print(RIN1k)


V12=ufloat(2.84,2.84*0.035)
V22=ufloat(1.30,1.30*0.035)
R2=ufloat(178.1e3,mme(178.1e3,"ohm"))

REQ2=(V22/(V12-V22))*R2

print(REQ2)
RIN10k = REQ2*RO/(RO-REQ2)
print(RIN10k)


