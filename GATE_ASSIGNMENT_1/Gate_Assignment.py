import numpy as np
from matplotlib import pyplot as plt

s = np.linspace(-np.pi,np.pi,1000000)
h = (-1)/(1+(s**2))
plt.plot(s,h,label='H(s)')
plt.grid()
plt.legend()
plt.xlabel('s')
plt.ylabel('H(s)')
