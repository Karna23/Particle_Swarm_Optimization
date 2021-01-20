#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:41:53 2020

@author: ee524
"""

import numpy as np
import matplotlib.pyplot as plt 
import math
import random



def grad(x,y):
   
    eta=0.2
   
    del_x = 2*np.exp(-.2*np.sqrt(.5*(x*x+y*y)))*x/np.sqrt(.5*(x*x+y*y))+np.pi*np.sin(2*x*np.pi)*np.exp(.5*(math.cos(2*np.pi*x)+math.cos(2*np.pi*y)))
   
    del_y = np.exp(-.2*np.sqrt(.5*(x*x+y*y)))*y/np.sqrt(.5*(x*x+y*y))+np.pi*np.sin(2*y*np.pi)*np.exp(.5*(math.cos(2*np.pi*x)+math.cos(2*np.pi*y)))
   
    x_new=x-eta*del_x
    y_new=y-eta*del_y
   
    return (x_new, y_new)

def functionvalue(x,y):    
    z = (-20 * math.exp(-0.2*(0.5*((x**2 +y**2))**0.5))) - math.exp(0.5 * (math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.exp(1) + 20 
    return z



x = np.arange(-10,10,0.2).tolist()
y = np.arange(-10,10,0.2).tolist()


z = np.zeros((100,100))

for i in range (0,100):
    for j in range(0,100):  
        z[i][j] = (-20 * math.exp(-0.2*(0.5*((x[i]**2 +y[j]**2))**0.5))) - math.exp(0.5 * (math.cos(2*math.pi*x[i]) + math.cos(2*math.pi*y[j]))) + math.exp(1) + 20


plt.contour(x,y,z)



omega = 0.05
fip = 0.5
fig = 1


S = 100
initx = np.zeros(S)
inity = np.zeros(S)
finalx = np.zeros(S)
finaly = np.zeros(S)
velocityx = np.zeros(S)
velocityy = np.zeros(S)
for i in range(0,100):
    initx[i] = random.uniform(-8,8)
    inity[i] = random.uniform(-8,8)
    finalx[i] = initx[i]
    finaly[i] = inity[i]

valuesinit = np.zeros(100)
valuesfinal = np.zeros(100)


for i in  range(0,100):
    valuesinit[i] = functionvalue(initx[i] ,inity[i])

for i in range(0,100):
    velocityx[i] = random.uniform(-20,20)
    velocityy[i] = random.uniform(-20,20)
    
maxiter = 90

velocity_x = 0 
velocity_y = 0
zinit = 0
zfinal = 0
for k in range(0,maxiter):
    for i in range(0,100):
        velocityx[i] = random.uniform(-20,20)
        velocityy[i] = random.uniform(-20,20)
    
    for i  in range( 0,100):
        rp = random.uniform(0,1)
        rg= random.uniform(0,1)
        velocity_x = omega * velocityx[i] + fip * rp * (finalx[i] - initx[i]) + fig * rg * (finalx[i] - initx[i] )
        velocity_y = omega * velocityy[i] + fip * rp * (finaly[i] - inity[i])+ fig * rg * (finaly[i] - inity[i] )
       # print("Velocity X :",velocity_x)
        #print("Velocity Y :",velocity_y)
        finalx[i] , finaly[i] = grad(initx[i] ,inity[i])
        zinit = functionvalue(initx[i],inity[i])
        zfinal = functionvalue(finalx[i] , finaly[i])
        
        initx[i] = finalx[i];
        inity[i] = finaly[i];
    plt.contour(x,y,z)
    plt.scatter(initx,inity , marker = 'x' , color = 'red')
    plt.show(block=False)
    plt.pause(0.3)
    plt.close()




