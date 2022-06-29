import numpy as np
tsa_2 = 0
r = int(input("Enter radius"))
tsa_1 = (4*22*(r**2))/7
vol = (4*22*(r**3))/(3*7)
for i in np.arange(1,r+1,0.1):
    tsa_2 += (2*22*i)/7
print ("Total surface area =",tsa_1,"Volume =",vol,"TSA_2 =",tsa_2 )
