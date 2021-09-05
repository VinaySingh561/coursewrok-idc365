# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:41:38 2021

@author: gamma
"""
import numpy as np
import matplotlib.pyplot as plt
X = []
X.append(1)

global i
for i in range(3,200):
    if i>1:
        for j in range(2,i):
            if (i%j ==0):
                break
        else:
               X.append(i)

print(set(X))
x = np.linspace(1,len(X), len(X))
print(x)
print(len(x),len(X))
plt.plot(x,X,"*")
 