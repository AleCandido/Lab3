from pylab import *
path = "C:\\Users\\Roberto\\Documents\\GitHub\\Lab3\\"
#path = "C:\\Users\\Studenti\\Desktop\\Lab3\\"
#path = "/home/alessandro/Documents/Università/3°anno/Laboratorio3/Lab3/"
sys.path = sys.path + [path]
from analyzer import *
import uncertainties
dir= path + "Esercitazione4\\"

#Guadagno per piccoli segnali

Vin, Vout = loadtxt(dir+"data/guadagnopiccolisegnali.txt", unpack= True)

dVin = Vin*0.035
dVout = Vout*0.035

Vin = unumpy.uarray(Vin, dVin)
Vout = unumpy. uarray(Vout, dVout)

index = arange(len(Vin))
Av = Vout/Vin
dAv = unumpy.std_devs(Av)
Av = unumpy.nominal_values(Av)

Afit, sigmaA = fit_const_yerr(Av, dAv)
dAfit = sqrt(sigmaA)

# plot

figure(1)
subplot(211)
title("Guadagno per piccoli segnali")
ylabel("guadagno")

errorbar(index, Av, dAv, fmt = "b,")
x = linspace(0, max(index), 1000)
y = linspace(Afit, Afit, 1000)
grid()
xticks(arange(0))
plot(x,y,"g")

# scarti normalizzati

subplot(212)
ylabel("scarti normalizzati")
grid()
xticks(arange(0))
plot(index, (Av-Afit)/dAv, ".", color="blue")
savefig(dir+"grafici/fit_guadagnopiccolisegnali.pdf")

#Chi quadro

chi = sum((Av-Afit)**2/dAv**2)
ndof = len(Av) - 1
print("\nFIT RESULT guadagno piccoli segnali\n")
print("Av = ", Afit, "\pm", dAfit)
print("chi / ndof =",chi,"/",ndof, "\n")


