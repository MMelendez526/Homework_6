from __future__ import division, print_function
#from vpython import *
from math import *
import numpy as np
from numpy import arange, pi, array
from pylab import plot, xlabel, ylabel, show, title, savefig

def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta*(np.pi/180)) #solves d-omega/dt
    return np.array([ftheta*180/np.pi, fomega], float) #Need to convert back to degrees

#Constants
g = 9.81 #gravity (m/s)
l = 0.08 #want an 8 cm arm length, but need to convert to meters

#Need to feed the initial conditions
a = 0.0 #starting time in seconds
b = 10 #ending time in seconds 
N = 10000 #number of steps
h = (b-a)/N #step-size

#Set up places for answers to go, with starting initial conditions
tpoints = arange(a, b, h)
xpoints = []
r = [89, 0.0]

#Leapfrog Method     
for t in tpoints:
    xpoints.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + k2, t + h)
    r += 0.5*k1 + k3
    
plot(tpoints, xpoints)
title('Modeling Nonliear Pendulum with Leapfrog Method')
xlabel('Time (seconds)')
ylabel('Angle (degrees)')
savefig('Pendulum_Leapfrog.eps')
show()

################    THIS PART ISN'T WORKING     ################
################  SOMETHING WRONG WITH VPYTHON  ################
#ball_1 = sphere(pos = vector(0,0,0), radius = 0.1)
#ball3 = sphere(pos = vector(0,0,0), radius = 0.1)
#pointer = arrow(pos = vector(0,0,0), axis = ball1.pos - ball3.pos, color = color.orange)
#
#thing = tpoints.size
#for i in range(thing):
#    rate(30)
#    xdiff = xpoints[i]
#    y = -cos(xdiff)
#    x = -sin(xdiff)
#    ball3.pos = vector(x,y,0)
#    pointer.pos = vector(x,y,0)
#    pointer.axis = ball1.pos - ball3.pos