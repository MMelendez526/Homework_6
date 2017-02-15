#Computational Homework #3, Problem #2 - Quadratic Equation

a = float(input('Please enter a: '))
b = float(input('Please enter b: '))
c = float(input('Please enter c: '))

############################################

x1 = (-b + ((b*b - 4*a*c)**(1/2)))/(2*a)
x2 = (-b - ((b*b - 4*a*c)**(1/2)))/(2*a)
x3 = (2*c)/(-b - ((b*b - 4*a*c)**(1/2)))
x4 = (2*c)/(-b + ((b*b - 4*a*c)**(1/2)))

print("The solutions to the equation in (a) are: ", x1, "and", x2) 
print("The solutions to the equation in (b) are:", x3, "and", x4)

#The above equations are equations given in part (a) and (b)

#The solutions to the equation in (a) are:  -9.999894245993346e-07 and -999999.999999
#The solutions to the equation in (b) are: -1.000000000001e-06 and -1000010.5755125057

#The solutions are clearly different, and this most likely comes from the 
#subtraction and the division in the equations in (a) and (b)

############################################

if b < 0:
    ep = -1
else:
    ep = 1
    
x5 = (-b - (ep*(b*b - 4*a*c)**(1/2)))/(2*a)
x6 = (2*c)/(-b - (ep*(b*b - 4*a*c)**(1/2)))

print("The roots of the quadratic eqation are: ", x5, "and", x6)

#The solution above should give the correct answer in all cases
#This solution comes from mixing the solutions in (a) and (b), and yields:
#The roots of the quadratic eqation are:  -999999.999999 and -1.000000000001e-06