#Homework #4, Prob #1
from random import random 
from numpy import arange
import matplotlib.pyplot as plt
#from pylab import plot, xlabel, ylabel, show
from matplotlib.legend_handler import HandlerLine2D

#Constants 
NBi213 = 10000 #inital number of Bi213 atoms
NTl = 0 #initial number of Tl209 atoms
NPb = 0 #initial number of Pb209 atoms
NBi209 = 0 #initial number of Bi209 atoms

tauBi = 46*60 #half-life of Bi213 in seconds
tauTl = 2.2*60 #half-life of Tl209 in seconds
tauPb = 3.3*60 #half-life of Pb209 in seconds

h = 1.0 #time-step in seconds
tmax = 20000 #end time in seconds

#Decay probabilities
pBi = 1 - 2**(-h/tauBi)
pTl = 1 - 2**(-h/tauTl)
pPb = 1 - 2**(-h/tauPb)
ppb_over_tl = 0.9791

#List of plot points
tpoints = arange(0.0, tmax, h)
Bi213points = []
Tlpoints = []
Pbpoints = []
Bi209points = []


#Main loop
for t in tpoints:
    Bi213points.append(NBi213)
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)
    Bi209points.append(NBi209)
       
    decay = 0 
    dec_to_pb = 0 
    for i in range(NBi213): 
        if random() < pBi: 
            decay += 1
            if random() < ppb_over_tl: 
                dec_to_pb += 1
    NBi213 -= decay
    NPb += dec_to_pb
    NTl += (decay - dec_to_pb) 

    decay = 0 
    for i in range(NTl):
        if random() < pTl: 
            decay += 1
    NTl -= decay
    NPb += decay

    decay = 0 
    for i in range(NPb):
        if random() < pPb: 
            decay += 1
    NPb -= decay
    NBi209 += decay
    

#Make the graph
line1, = plt.plot(tpoints, Tlpoints, label = 'Tl 209')
line2, = plt.plot(tpoints, Pbpoints, label = 'Pb 209')
line3, = plt.plot(tpoints, Bi213points, label = 'Bi 213')
line4, = plt.plot(tpoints, Bi209points, label = 'Bi 209')
plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.xlabel("Time (seconds)")
plt.ylabel("Number of atoms")
plt.title('Radioactive Decay of Bi 213')
plt.savefig('Bi_Decay.eps')
plt.show()