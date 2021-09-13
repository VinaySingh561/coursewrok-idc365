# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:43:16 2021

@author: gamma
"""
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
x_array = np.array([3,4,5,6,7,8,9,10])
y_array = np.array([1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10])
f = interpolate.interp1d(x_array, y_array)


x = np.linspace(3,10,15)

y= 1/x
print(y)
plt.plot(x, y, "b*", label="1/x")
P2 = f(x)
plt.plot(x,P2, "r.",label = "P2")
plt.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})