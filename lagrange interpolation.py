# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:47:11 2021

@author: gamma


"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams;rcParams['figure.figsize'] = 5, 5

def Lagarange_intrpolate(x_array,y_array,x):
    n = len(x_array)
    ans = 0
    for j in range((n)):
        numr= 1
        denm= 1
        for i in range(n):
            if (i !=j):
                numr *= x-x_array[i]
                denm *= x_array[j]-x_array[i]
        lagr = numr/denm
        ans += lagr*y_array[j]         
    return ans        



P2 = np.zeros(10)
fig = plt.figure(figsize = (5,5))



     
ax1 = fig.add_subplot(2,2,1)
x_array = np.array([3,4])
y_array = np.array([1/3,1/4])
x = np.linspace(0.5,7,10)
y= 1/x
ax1.plot(x, y, "b", label="1/x")

for i in range(len(x)):
    P2[i] = Lagarange_intrpolate(x_array, y_array, x[i])

ax1.plot(x,P2,"r.", label = "$P2(3,4)")
ax1.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})



ax2 = fig.add_subplot(2,2,2)
x_array = np.array([3,4,5])
y_array = np.array([1/3,1/4,1/5])
x = np.linspace(0.5,7,10)
y= 1/x
ax2.plot(x, y, "b", label="1/x")

for i in range(len(x)):
    P2[i] = Lagarange_intrpolate(x_array, y_array, x[i])

ax2.plot(x,P2,"r.", label = "$P2(3,4,5)")
ax2.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})


ax3 = fig.add_subplot(2,2,3)
x_array = np.array([2,3,4])
y_array = np.array([1/2,1/3,1/4])
x = np.linspace(0.5,7,10)
y= 1/x
ax3.plot(x, y, "b", label="1/x")

for i in range(len(x)):
    P2[i] = Lagarange_intrpolate(x_array, y_array, x[i])

ax3.plot(x,P2,"r.", label = "$P2(2,3,4)")
ax3.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})


ax4 = fig.add_subplot(2,2,4)
x_array = np.array([2,3,4,5])
y_array = np.array([1/2,1/3,1/4,1/5])
x = np.linspace(0.5,7,10)
y= 1/x
ax4.plot(x, y, "b", label="1/x")

for i in range(len(x)):
    P2[i] = Lagarange_intrpolate(x_array, y_array, x[i])

ax4.plot(x,P2,"r.", label = "$P2(2,3,4,5)")
ax4.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})





