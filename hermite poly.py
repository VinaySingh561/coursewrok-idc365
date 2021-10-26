# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:20:50 2021

@author: gamma
"""
#Choose simple units
m=1.
w=1.
hbar=1.



import numpy as np
import numpy.polynomial.hermite as Herm
import math
import matplotlib
import matplotlib.pyplot as plt 
def hermite(x,n):
    xi = np.sqrt(m*w/hbar)*x
    herm_coeffs = np.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
#Discretized space
dx = 0.05
x_lim = 12
x = np.arange(-x_lim,x_lim,dx)


def stationary_state(x,n):
    xi = np.sqrt(m*w/hbar)*x
    prefactor = 1./math.sqrt(2.**n * math.factorial(n)) * (m*w/(np.pi*hbar))**(0.25)
    psi = prefactor * np.exp(- xi**2 / 2) * hermite(xi,n)
    return psi

#plt.figure()
#plt.plot(x, stationary_state(x,4))
#plt.xlabel(r"x")
#plt.ylabel(r"$\psi_4(x)$")
#plt.title(r"Test Plot of $\psi_4(x)$")
#plt.show()