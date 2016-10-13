from pylab import *
import numpy as np

x = linspace(0.001, 2, 1000)

def f(x):
    return 20*log10(sqrt(x**2/(x**2 + 4)))
    
vf = np.vectorize(f)
y = vf(x)
plot(x, y)

show()

from uncertainties import *

(a,b)=correlated_values_norm([(-0.04,0.03),(0.11,0.11)],[[ 1.,-0.97588732],[-0.97588732,1. ]])

(c,d)=correlated_values_norm([(-0.908,0.016),(4.68,0.13)],[[ 1.,-0.98950397],[-0.98950397,1.]])

print(e**((d-b)/(a-c)))