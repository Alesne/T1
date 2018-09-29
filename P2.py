#p2
import math
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
mp.rcParams['xtick.labelsize'] = 15
mp.rcParams['ytick.labelsize'] = 15
datos = np.loadtxt('firas_monopole_spec_v1.txt')
h = 6.62607004e-34 #J*s
c = 299792458.0 #m/s
k_b = 1.38064852e-23 #J/K
T = 2.725 #K
frecuency=[]   #1/cm
FIRAS=[]       #MJy/sr
residual=[]    #kJy/sr
uncertainty=[] #kJy/sr
galaxy=[]      #kJy/sr

for i in datos:
    frecuency=datos[:,0]
    FIRAS=datos[:,1]
    residual=datos[:,2]
    uncertainty=datos[:,3]
    galaxy=datos[:,4]
#parte 1
meanf = np.mean(frecuency)
for k in frecuency:
    suma=(k - meanf)**2
errorf = (suma/(43*42))**(1/2)*100
fig, bx = plt.subplots()
plt.plot(frecuency,uncertainty, color='g', label='Incertidumbre')
bx.errorbar(frecuency,FIRAS,yerr=errorf)
plt.xlabel('$Frecuencia[1/cm]$', fontsize=15)
plt.ylabel('$Intensidad[MJy/sr]$', fontsize=15)
plt.show()
#parte 2
frecuency=(frecuency/100)*c #(1/m)*(m/s) = 1/s
#metodo simpson 1/3
n = 100
eps = 43/100
#sumatorias
a = 0
b = 0
for i in range(n//2 - 1):
    a= a + ((np.tan(2*i + 1)**3)*(np.tan(2*i + 1)**2 + 1)) / (np.e(np.tan(2*i + 1)) - 1)
for j in range(n//2 - 1):
    b= b + ((np.tan(2*j)**3)*(np.tan(2*j)**2 + 1)) / (np.e(np.tan(2*j)) - 1)
#integral
I = (eps/3)*(((np.tan(np.pi/2)**3)*(np.tan(np.pi/2)**2 + 1)) / (np.e(np.tan(np.pi/2)) - 1) + 4*a + 2*b)

print (I,(np.pi**4)/15)
#fig, ax = plt.subplots()
#ax.errorbar(x, y)