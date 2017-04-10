from math import sin
import numpy as np
from numpy import arange, pi
from pylab import plot, xlabel, ylabel, show, title, savefig

#Constants
g = 9.81 #gravity (m/s)
l = 0.08 #want an 8 cm arm length, but need to convert to meters

#Define the function that describes the motion of the pendulum
def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta*(np.pi/180)) #solves d-omega/dt; convert to radians for sin
    return np.array([ftheta*180/np.pi, fomega], float) #Need to convert back to degrees

#Need to feed initial conditions
a = 0.0 #starting time in seconds
b = 10 #ending time in seconds 
N = 1000 #number of steps
h = (b-a)/N #step-size

#Set up places for answers to go, with starting initial conditions
tpoints = arange(a, b, h)
xpoints = []
r = [-179, 0.0]

#4th order Runge-Kutta Method
for t in tpoints:
    xpoints.append(r[0])
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6

plot(tpoints, xpoints)
title('Modeling Nonlinear Pendulum with Runge-Kutta')
xlabel('time (in seconds)')
ylabel('x(t) - angle (in degrees)')
savefig('Pendulum_RK.eps')
show()