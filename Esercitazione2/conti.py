from pylab import *
import numpy as np

x = linspace(0.001, 4, 1000)

def f(x):
    return (sqrt((x**2+400)/(x**2 + 4)))
    
vf = np.vectorize(f)
y = vf(x)

title("Rapporto segnale/rumore")
xlabel("Frequenza di taglio [kHz]")
ylabel("Rapporto segnale/rumore")
plot(x, y)
show()
savefig(directory+"grafici/scarti_"+fig+".pdf")