#Computational Homework #3, Problem #4

import math
import numpy as np
import matplotlib.pyplot as plt

xaxis = np.linspace(0.0, 3.0, 31, endpoint = True)

Ex = []

def ex(x):
    return math.e**(x**2)

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

for x in frange(0, 3.1, 0.1):
    N = 1000
    a = 0
    b = x
    h = (b-a)/N

    s = 0.5*ex(b)
    for k in range(1,N):
        s += ex(a+k*h)
        
    EX = s*h
    EX2 = round(EX, 4)
    Ex.append(EX2)

#print(Ex)
    
plt.plot(xaxis, Ex)
plt.title('$E(x)$')
plt.xlabel('x')
plt.ylabel('$E(x) = \int_{0}^{x} e^{t^2} dt$')
plt.savefig('E(x).eps')
plt.show()

##############################################
#When I print out the values of E(x) I get, along with the graph, the following:
#[0.0, 0.1003, 0.2026, 0.3091, 0.4222, 0.5447, 0.6802, 0.833, 1.0087, 
#1.215, 1.4622, 1.7641, 2.1404, 2.6191, 3.2402, 4.0624, 5.1728, 6.7027, 
#8.8535, 11.9382, 16.4517, 23.1896, 33.4516, 49.3973, 74.6757, 115.5603, 
#183.0238, 296.5976, 491.6664, 833.4865, 1444.5801]