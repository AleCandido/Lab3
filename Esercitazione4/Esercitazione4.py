from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione3\\"
###########################################################################

Vin, Vout = loadtxt("data/guadagnopiccolisegnali.txt", unpack= True)

dVin = mme(Vin, "volt")
dVout = mme(Vout, "volt")

Vin = unumpy.uarray(Vin, dVin)
Vout = unumpy. uarray(Vout, dVout)

index = arange(len(Vin))
Av = Vout/Vin

fit_const_yerr(unumpy.nominal_values(Av), unumpy.std_devs(Av))

errorbar(index, unumpy.nominal_values(Av), unumpy.std_devs(Av))
