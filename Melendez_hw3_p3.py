#Computational Homework #3, Problem #3
#Calculate the heat capacity of a solid

import math
import matplotlib.pyplot as plt
import numpy as np

V = 0.001 #in m^3
p =  6.022e28 #in m^-3
theta = 428 #in K
k = 1.38e-23    

T = float(input('Please enter the desired temperature: '))

CV = (9*V*p*k)*((T/theta)**3)

def C(x):
    return ((x**4)*(math.e**x))/(((math.e**x)-1)**2)
    
N = 1000 #Number of steps in integration
a = 0.00 #lower integration bound
b = theta/T #upper integration bound
h = (b-a)/N

s = 0.5*C(b)
for j in range (1, N):
    s += C(a+j*h)

print("The Heat Capacity for a Solid at a Temperature of ", T, "K is: ", round(CV*h*s, 3))

Temp = np.linspace(5,500, 495, endpoint = True)
temp = []
for T in range(5, 500):
    N = 1000
    a = 0.00
    b = theta/T
    h = (b-a)/N

    CV = (9*V*p*k)*((T/theta)**3)
    
    s2 = 0.5*C(b)
    for m in range (1, N):
        s2 += C(a+m*h)
    
    tem = s2*CV*h
    temp.append(tem)

plt.plot(Temp, temp)
plt.title('Heat Capacity of a Solid')
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity')
plt.savefig('Heat_Capacity.eps')
plt.show()

###########################################
#Aside from the graph, the code yields the following:

#Please enter the desired temperature:
#If I put in, say 100, then I return:
#The Heat Capacity for a Solid at a Temperature of  100.0 K is:  1152.722