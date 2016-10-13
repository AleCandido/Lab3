from uncertainties import *

(a,b)=correlated_values_norm([(-0.04,0.03),(0.11,0.11)],[[ 1.,-0.97588732],[-0.97588732,1. ]])

(c,d)=correlated_values_norm([(-0.908,0.016),(4.68,0.13)],[[ 1.,-0.98950397],[-0.98950397,1.]])

print(e**((d-b)/(a-c)))