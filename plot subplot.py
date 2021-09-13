# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:10:10 2021

@author: gamma
"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams;rcParams['figure.figsize'] = 5, 5
x1 = np.linspace(-1,1,40);y1 = x1**2;y2 = x1**3;
y3 = x1**4;y4 = x1**5
fig = plt.figure(figsize = (5,5))
ax1= fig.add_subplot(2,2,1)

ax1.plot(x1,y1,"r.", label = "$y= x^2$")
ax1.legend(loc = "upper center",fancybox=True, shadow=True, prop={'size':'small'})
ax1.xaxis.set_major_locator(plt.MaxNLocator(3))

ax2= fig.add_subplot(2,2,2)
ax2.plot(x1,y2,"r.", label = r"$y= x^3$")
ax2.legend(loc = 'upper center', fontsize = 10,fancybox=True, shadow=True, prop={'size':'small'})
ax3=fig.add_subplot(2,2,3)
ax3.plot(x1,y3,"r.", label = r"$y= x^4$")
ax3.legend(loc = 'upper center',fancybox=True, shadow=True, prop={'size':'small'})
ax4= fig.add_subplot(2,2,4)
ax4.plot(x1,y4,"r.", label = r"$y= x^5$")
ax4.legend(loc = 'upper center',fancybox=True, shadow=True, prop={'size':'small'})



ax1.x1axis.set_major_locator(plt.MaxNLocator(6))