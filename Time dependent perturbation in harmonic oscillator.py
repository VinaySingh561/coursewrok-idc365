# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:46:37 2021

@author: gamma
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

import numpy.polynomial.hermite as Herm
import math
m=1.
w=1.
hbar=1. 
def hermite(x,n):
    xi = np.sqrt(m*w/hbar)*x
    herm_coeffs = np.zeros(n+1)
    herm_coeffs[n] = 1
    return Herm.hermval(xi, herm_coeffs)
#Discretized space
dx = 0.05
x_lim = 12
x = np.arange(-x_lim,x_lim,dx)

import scipy.integrate as integrate
Cf_1 = np.zeros((5,5)) #first order transistion coefficient
CF_1 = np.zeros(5)
time = np.zeros(5)
fvi = np.zeros(5)



def stationary_state(x,n):
    xi = np.sqrt(m*w/hbar)*x
    prefactor = 1./math.sqrt(2.**n * math.factorial(n)) * (m*w/(np.pi*hbar))**(0.25)
    psi = prefactor * np.exp(- xi**2 / 2) * hermite(xi,n)
    return psi


def perturbation(f,w_p,i,t):
    
    result = integrate.quad(lambda x: stationary_state(x, f)* np.exp(complex(0,1)*w_p*t)*stationary_state(x, i),-1 ,1)
    return result[0]

   
# function that returns dy/dt
def model(y,t):
    global w_per
    w_per = 1
    dydt = -perturbation(0,w_per,0,t)*y
    return dydt
#intial conditions
y0 = 1
# time points
t = np.linspace(0,20)
y = odeint(model,y0,t)
print(len(t))
print(y[25])
def model_1(y_one,t):
   
    dy_onedt = abs(-(perturbation(1,w_per,0,t)*np.exp(complex(0,1)*w_per*t))-perturbation(1,w_per,1,t)*y_one)
    return dy_onedt
    

# initial condition

y_one0 = 0



# solve ODE

y_one = odeint(model_1,y_one0,t)
print(y_one)

# plot results
plt.plot(t,y_one, label = "transistion coeffiecient of order first at w=1 and w_per = " + str(w_per) )
plt.xlabel('time')
plt.ylabel('C_1(t)')
plt.legend(loc = "best",fancybox=True, shadow=True, prop={'size':'small'})
plt.show()