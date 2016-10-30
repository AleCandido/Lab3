from uncertainties import *
import math

(a,b)=correlated_values_norm([(16.4 , 1.2),(-10.8 , 1.6)], [[ 1.,-0.98690812],[-0.98690812 ,1.]])
(c,d)=correlated_values_norm([(0.36 , 0.27),(18.0 , 0.9)], [[ 1.,-0.98450515],[-0.98450515 ,1.]])

print(10**((d-b)/(a-c)))

###########################################

# PASSA-BANDA RETTE 1-2#

(a,b)=correlated_values_norm([(0.36 , 0.27),(18.0 , 0.9)], [[ 1.,-0.98450515],[-0.98450515 ,1.]])

(c,d)=correlated_values_norm([(-17.9 , 0.7),(107. , 4.)], [[ 1.,-0.99836208],[-0.99836208,1.]])

print(10**((d-b)/(a-c)))