import math
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np
mp.rcParams['xtick.labelsize'] = 13
mp.rcParams['ytick.labelsize'] = 13
#metodo sencillo clases
x = 1.004
h = np.logspace(-1, -16, 16, base=10.)
dfx = -(np.cos(x + h) - np.cos(x)) / h
#metodo tarea
sen = math.sin(x)
#plot metodo sencillo
plt.plot(h, dfx - sen)
plt.title('Comparacion metodo sencillo')
plt.xscale('log')
plt.axhline(0, color='0.8')
plt.xlabel('$h$', fontsize=20)
plt.ylabel('$\\frac{d}{dx}f(x) - sin(x)$', fontsize=20)
_ = plt.xticks(h[::2])
#plot metodo tarea
dgx = (np.cos(x+2*h)-8*np.cos(x+h)+8*np.cos(x-h)-np.cos(x-2*h))/12*h
plt.subplot(h, dgx - sen)
plt.title('Comparacion metodo orden(h^4)')
plt.xscale('log')
plt.axhline(0, color='0.8')
plt.xlabel('$h$', fontsize=20)
plt.ylabel('$\\frac{d}{dx}g(x) - sin(x)$', fontsize=20)
_ = plt.xticks(h[::2])
