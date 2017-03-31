import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import math

x, y = np.loadtxt('munich_2.txt', unpack = True)

plt.plot(x, y)
plt.xlabel('Time (years)')
plt.ylabel('Temperature')
plt.show()

guess_amplitude = 14.0
guess_phase = math.pi-0.2
guess_offset = np.mean(y)

p0 = [guess_amplitude, guess_phase, guess_offset]

def my_cos(x, amplitude, phase, offset):
    return amplitude*np.cos(2*x*math.pi + phase) + offset

#now do the fit
fit = curve_fit(my_cos, x, y, p0=p0)

#do our first estimate
data_first_guess = my_cos(x, *p0)

#recreate fitted curve using optimized fitting parameters
data_fit = my_cos(x, *fit[0])


plt.plot(x, y)
plt.plot(x, data_first_guess, 'r')
plt.xlabel('Time (years)')
plt.ylabel('Temperature (Celsius)')
plt.title('Temperature in Munich')
plt.savefig('Munich.eps')
plt.show()

print('The best-fit values for the parameters are as follows: a = ', guess_amplitude\
      , ', b = ', round(guess_phase, 3), ', and c = ', round(guess_offset, 4))
print('The overall average temperature of Munich is: ', round(guess_offset, 4), 'degrees Celsius')
print('According to the model, the hottest temperature is: ', round(max(data_first_guess), 4), 'degrees Celsius')
print('According to the model, the coldest temperature is: ', round(min(data_first_guess), 4), 'degrees Celsius')


##################################################
#ANSWERS/OUTPUT
#  (a) The best-fit values for the parameters are as follows: a =  14.0 , b =  2.942 , and c =  9.4403
#      The plot of the data and fitted model is shown separately
#  (b) The overall average temperature of Munich is:  9.4403 degrees Celsius
#      According to the model, the hottest temperature is:  23.4402 degrees Celsius
#      According to the model, the coldest temperature is:  -4.5594 degrees Celsius
#  (c) The meaning of the b parameter is the left-right shift of the cosine function.
#      The value does make sense, because without it the cosine term will be at its maximum
#      value at the beginning of the year according to the model, which we know is incorrect