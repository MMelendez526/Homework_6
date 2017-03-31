import fitsio
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = fitsio.FITS("SpO-dr13.fits")

#Sort out the data based on the SDSS site
good= data[1].where("ZWARNING == 0 && 22.5 - (2.5 * log10(SPECTROFLUX[3])) <= 22.2")
Z_err = data[1]["Z_ERR"][good]
Sflux = data[1]["SPECTROFLUX"][good] #spflux_1
Z_arr = data[1]["Z"][good] #z_arr_1

#Filtering out objects without a "reasonable" z_err value.
Z_err_1 = np.logical_and(Z_err < 1, Z_err > 0)

Z_err = Z_err[Z_err_1]
Sflux_1 = Sflux[Z_err_1]
Z_arr_1 = Z_arr[Z_err_1]

#Converting from nanomaggies, because the data is stupid
SFlux = 22.5 - (2.5 * np.log10(Sflux_1))

#Select the target stars with only a certain color
SP = np.logical_and((SFlux[:,3]-SFlux[:,4]) > 0.5, (SFlux[:,3]-SFlux[:,4]) < 0.55)

#Pick the data we want
z_err_2 = Z_err[SP]
SPF = SFlux[SP]
z_arr_2 = Z_arr_1[SP]

SP_flux = SPF[:,3]
z_arr = z_arr_2

def lin(x, slope, int_1):
	return slope * x + int_1

def quad(x, a, b, int_2):
	return a * x**2 + b*x + int_2

def broken(xvals, x, y):
	return np.interp(xvals, x, y)

popt1, pcov1 = curve_fit(lin, z_arr, SP_flux, sigma = z_err_2)
popt2, pcov2 = curve_fit(quad, z_arr, SP_flux, sigma = z_err_2)

#############################################
#Print out the parameters of the best-fit functions
print("Linear Best-Fit Values:")
print("Slope: {0:.3f}".format(popt1[0]))
print("Intercept: {0:.3f}".format(popt1[1]))
print('\n')
print("Quadratic Best-Fit Values:")
print("a: {0:.3f}".format(popt2[0]))
print("b: {0:.3f}".format(popt2[1]))
print("c: {0:.3f}".format(popt2[2]))

#############################################
xvals = np.linspace(min(z_arr), max(z_arr), 3*(max(z_arr)-min(z_arr)))
broken_y_fit = broken(xvals,z_arr,SP_flux)

x11 = np.sort(z_arr)
y11 = popt1[0]*np.sort(z_arr) + popt1[1]
y22 = popt2[0]*np.sort(z_arr)**2 + popt2[1]*np.sort(z_arr) + popt2[2]

#############################################
#Plot data
plt.errorbar(z_arr, SP_flux, xerr = z_err_2, fmt='None')
plt.plot(xvals, broken_y_fit, 'r', label = "Broken Linear")
plt.plot(x11, y11, 'y', label = "Linear")
plt.plot(x11, y22, 'g', label = "Quadratic")
plt.legend(loc = 3)
plt.xlabel('Redshift')
plt.ylabel('Magnitude')
plt.savefig('SDSS.eps')
plt.savefig('SDSS.png')
plt.show()

#############################################################################
#ANSWERS
# A -OUTPUT FROM CODE
#Linear Best-Fit Values:
#Slope: 5.063
#Intercept: 17.453

#Quadratic Best-Fit Values:
#a: -2.175
#b: 6.802
#c: 17.305


# B - Which function fits the data best
#The broken linear is the best fit; I can't really tell where it is 'broken' because
#it looks like just a straight line, but whatevs. The data doesn't look super linear
#according to the blue colored data; the linear function is definitely not right
#and the quadratic function is arguably just as bad, if not worse of a fit.
#We would expect the broken linear function to fit the data best