# coding: utf-8
from uncertainties import *
from pylab import *
cm =  [[1.,  0.61210657, -0.66267107],
 [0.61210657 , 1., -0.37495779],
 [-0.66267107, -0.37495779, 1.]]
(a,b,c) = correlated_values_norm([(1.01e+06 , 5.e+04), (4.84e+05 , 1.0e+04), (1.0764 , 0.0024)], cm)

# la matrice di correlazione e i parametri sono il risultato di un fit

f1 = (b + (b**2 - 4*a)**0.5)/2
f2 = (b - (b**2 - 4*a)**0.5)/2

# sono le frequenze di taglio del derivatore, infatti a e b rappresentano il prodotto e la somma
