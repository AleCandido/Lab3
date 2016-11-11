# coding: utf-8
from analyzer import *
mme(6.24e-3, 'ampere')
idss = uncertainties.ufloat(6.24e-3,mme(6.24e-3, 'ampere'))
idss * 1000
idss
from uncertainties import *
vp = ufloat(2.198, 0.025)
vp
vgs = ufloat(0.650, 0.004)
vgs
idss*(vgs/vp - 1)**2
Id = idss*(vgs/vp - 1)**2
Id
Id*1000
idm = ufloat(3.07, 0.04)
idm
gm = 2*(idm*idss)**(0.5)/vp
gm
idm = ufloat(3.07e-3, 0.04e-3)
gm = 2*(idm*idss)**(0.5)/vp
gm
Id
gm
Id*100
Id*1000
gm*1000
mme(677e3, 'ohm')
mme(677e3, 'ohm')
