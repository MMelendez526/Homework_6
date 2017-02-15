#Computational Homework #3, Problem #1
#Need to plot a .txt file and give it a color scheme 

from pylab import imshow, show
import matplotlib.pyplot as plt

data = loadtxt("stm.txt", float)
imshow(data)
plt.savefig('silicon_density.eps')