from BobLightyear import *

# Slew rate, misurato con Schmitt$

dvs = umme(20.6, 'volt', 'osc')
dvd = umme(13, 'volt', 'osc')
dvdf = umme(7.4, 'volt', 'osc')

dts = umme(1.8e-6, 'time', 'osc')
dtd = umme(1e-6, 'time', 'osc')
dtdf = umme(0.5e-6, 'time', 'osc')

sls = dvs/dts
sld = dvd/dtd
sldf = dvdf/dtdf

print("\n")
print("slew rate in salita:", sls)
print("slew rate in discesa:", sld)
print("slew rate in discesa forte:", sldf)
print("\n")
