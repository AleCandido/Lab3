# coding: utf-8
from uncertainties import *
from pylab import *
cm =  [[ 1.    ,      0.60839744, -0.66077541],
 [ 0.60839744 , 1.   ,      -0.37562886],
 [-0.66077541, -0.37562886 , 1.        ]]
(a,b,c) = correlated_values_norm([(9.8e+05 , 9.e+04), (4.87e+05 , 1.9e+04), (1.077 , 0.005)], cm)

# la matrice di correlazione e i parametri sono il risultato di un fit

f1 = (b + (b**2 - 4*a)**0.5)/2
f2 = (b - (b**2 - 4*a)**0.5)/2

print("\nfreq. passa basso:", f1, "\nfreq derivatore:", f2, "\n")

# sono le frequenze di taglio del derivatore, infatti a e b rappresentano il prodotto e la somma
