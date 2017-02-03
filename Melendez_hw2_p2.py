#Comp homework 2, problem 2

A = int(input('Please enter A: '))
Z = int(input('Please enter Z: '))
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

if (A % 2 == 0): 
    if (Z % 2 == 0):
        a5 = 12
    else:
        a5 = -12
else:
    a5 = 0

B = (a1*A) - (a2*(A**(2/3))) - (a3*((Z**2)/(A**(1/3)))) - ((a4*((A-(2*Z))**2))/(A))\
- (a5/(A**(1/2)))
nuc = B/A

print('The Binding Energy for an atomic nucleus with atomic number', Z, 'and \
mass number', A, 'is: ', round(B,3), 'MeV')

print('The binding energy per nucleon is: ', round(nuc,3), 'MeV')


####################################
#           ANSWERS
####################################


#FOR A = 58, Z = 28

#Please enter A: 58
#Please enter Z: 28
#The Binding Energy for an atomic nucleus with atomic number 28 and mass number 58 is:  490.784 MeV
#The binding energy per nucleon is:  8.462 MeV


#FOR A = 59, Z = 28

#Please enter A: 59
#Please enter Z: 28
#The Binding Energy for an atomic nucleus with atomic number 28 and mass number 59 is:  498.145 MeV
#The binding energy per nucleon is:  8.443 MeV


#FOR A = 58, Z = 27

#Please enter A: 58
#Please enter Z: 27
#The Binding Energy for an atomic nucleus with atomic number 27 and mass number 58 is:  485.309 MeV
#The binding energy per nucleon is:  8.367 MeV