from pylab import *
import numpy as np

x = linspace(0.001, 2, 1000)

def f(x):
    return 20*log10(sqrt(x**2/(x**2 + 4)))
    
vf = np.vectorize(f)
y = vf(x)
plot(x, y)

show()