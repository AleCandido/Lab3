from pylab import *
#path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione3\\"
###########################################################################

#Guadagno per piccoli segnali

Vin, Vout = loadtxt("data/guadagnopiccolisegnali.txt", unpack= True)

dVin = mme(Vin, "volt")
dVout = mme(Vout, "volt")

Vin = unumpy.uarray(Vin, dVin)
Vout = unumpy. uarray(Vout, dVout)

index = arange(len(Vin))
Av = Vout/Vin

Afit = fit_const_yerr(unumpy.nominal_values(Av), unumpy.std_devs(Av))

figure(1)

errorbar(index, unumpy.nominal_values(Av), unumpy.std_devs(Av))
x = linspace(0, max(index), 1000)
y = linspace(Afit, Afit, 1000)
plot(x,y)
# volendo poi si plottano anche gli scarti normalizzati

###########################################################################
