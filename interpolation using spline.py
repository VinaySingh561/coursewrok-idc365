# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:08:40 2021

@author: gamma
"""
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (7,7))
ax1 = fig.add_subplot(2,2,1)
x_array = np.array([2,3,4,5])
y_array = np.array([1/2,1/3,1/4,1/5])
tck = interpolate.splrep(x_array, y_array)


x = np.arange(2,5.1,0.1)

y= 1/x
print(y,len(y))
ax1.plot(x, y, "b", label="1/x")
P2 = interpolate.splev(x,tck)
print(P2)
type(P2)
ax1.plot(x,P2, "r.",label = "P2(Spline points)")


ax1.set_xlabel('x')
ax1.set_ylabel('y(x)')
ax1.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})




##error calculation
ax2 = fig.add_subplot(2,2,2)
x = np.arange(2,5.1,0.1)
error = []
for i in range(len(y)):
    err = P2[i]-y[i]
    error.append(err)
    
print(error)

ax2.plot(x,error, "r.",label = "error")

ax2.set_xlabel('x')

ax2.set_ylabel('error using spline(x)')
ax2.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})


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

ax3 = fig.add_subplot(2,2,3)
x_array = np.array([2,3,4,5])
y_array = np.array([1/2,1/3,1/4,1/5])
x = np.arange(2,5.1,0.1)
y= 1/x
ax3.plot(x, y, "b", label="1/x")
P4 = np.zeros(31)
for i in range(len(x)):
    P4[i] = Lagarange_intrpolate(x_array, y_array, x[i])

ax3.plot(x,P4,"r.", label = "$P4(2,3,4,5)")
ax3.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})



ax4 = fig.add_subplot(2,2,4)
x = np.arange(2,5.1,0.1)
error1 = []
for i in range(len(y)):
    err = P4[i]-y[i]
    error1.append(err)
    
print(error)

ax4.plot(x,error1, "r.",label = "error")
ax4.plot(x,error, "r.",label = "error")

ax4.set_xlabel('x')

ax4.set_ylabel('error1(x)')
ax4.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})













ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
fig.suptitle('Interpolation')