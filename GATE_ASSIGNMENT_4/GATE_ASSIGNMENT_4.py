# -*- coding: utf-8 -*-
"""GATE_ASSIGNMENT_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jftxx89dYKbNoNpRyRQSyNnZJGg9T-uX
"""

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
fig, ax = plt.subplots()
# setting the x - coordinates
x = np.arange(-20, 30, 0.1)
# setting the corresponding y - coordinates
y = (x-1)/((x-1)**2 + 1**2)

label = plt.axvline(x=1,label="x=a",color='red')
'''x1= 2
y1 = np.arange(-20, 30, 0.1)'''
# plotting the points
#plt.plot(x, y,'orange')
'''plt.plot(x1,y1)'''
plt.xlim(-5,10)
plt.annotate("a", (1+0.02, 0+0.01))
plt.annotate("a+ia", (1+0.02, 1+0.01))
plt.annotate("a-ia", (1+0.02, -1+0.01))
line1 = 1 # vertical x = 3
line2 = 50 # vertical x = 5
zero, = plt.plot(1,0, 'ro',label = 'Zeros',color='green')
pole, = plt.plot(1,1, '*',label = 'poles',color='black')
pole, = plt.plot(1,-1, '*',label = 'poles',color='black')
ax.axvspan(line1, line2, alpha=.5, color='blue')
patches = mpatches.Patch(color="blue", label="ROC")
plt.legend(handles=[patches,label,zero,pole], loc = 'upper right')
plt.xlabel("Re{s}")
plt.ylabel("iW")
# function to show the plot
plt.grid()
plt.show()
#There are two complex poles
