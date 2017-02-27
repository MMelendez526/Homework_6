from numpy import exp
from random import random

N = int(1000000) #steps
int_val = 2  #value of the integral given in the book

def p_rand():
	rand_val = (random())**2
	return rand_val

int_sum = float(0)

for xx in range(N):
	temp = p_rand()  # Need to save the random number for use in importance sampling formula
	f_x = (temp**(-1 / 2)) / (exp(temp) + 1)
	w_x = temp**(-1 / 2)

	int_sum += (f_x / w_x)

I = (1 / N) * int_sum * int_val  #Equation 10.42 from book; shows importance sampling

print(I)