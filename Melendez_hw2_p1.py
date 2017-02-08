#Comp Homework 2, Problem 1
#Spaceship traveling (v) to planet (x) ly away
#Input speed v as fraction of c and print out time in years to get there

v = float(input('Please enter the speed of the ship in terms of the speed of light \
(such as in, "the speed of the ship is 0.90c"):'))

d = float(input('Please enter the distance that the ship is traveling (in light \
years): '))

dist = d*9.461e15 #Need to multiply by number of meters in a light-year
c = 3e8

Obt = dist/(v*c)
Pst = (dist/(v*c))*((1-(v**2))**(1/2))

Obts = Obt/(3.154e7)
Psts = Pst/(3.154e7)
#Time would be in seconds, so need to convert it to years (denominator)


print('The time it would take for a ship to travel', d, 'light years at a speed\
 of', v, 'c as percieved by an observer is: ', round(Obts, 5), 'years')

print('The time it would take for a ship to travel', d, 'light years at a speed\
 of', v, 'c as percieved as a passenger on the ship is: ', round(Psts,5), 'years')

####################################
#           ANSWERS
####################################

#FOR SPEED OF 0.9c

#Please enter the speed of the ship in terms of the speed of light (such as in, 
#"the speed of the ship is 0.90c"):0.90
#Please enter the distance that the ship is traveling (in light years): 10
#The time it would take for a ship to travel 10.0 light years at a speed of 0.9 c 
#as percieved by an observer is:  11.10994 years
#The time it would take for a ship to travel 10.0 light years at a speed of 0.9 c 
#as percieved as a passenger on the ship is:  4.84271 years


#FOR SPEED OF 0.98c

#Please enter the speed of the ship in terms of the speed of light (such as in, 
#"the speed of the ship is 0.90c"):0.98
#Please enter the distance that the ship is traveling (in light years): 10
#The time it would take for a ship to travel 10.0 light years at a speed of 0.98 c 
#as percieved by an observer is:  10.203 years
#The time it would take for a ship to travel 10.0 light years at a speed of 0.98 c 
#as percieved as a passenger on the ship is:  2.03037 years


#FOR SPEED OF 0.999c

#Please enter the speed of the ship in terms of the speed of light (such as in, 
#"the speed of the ship is 0.90c"):0.999
#Please enter the distance that the ship is traveling (in light years): 10
#The time it would take for a ship to travel 10.0 light years at a speed of 0.999 c 
#as percieved by an observer is:  10.00895 years
#The time it would take for a ship to travel 10.0 light years at a speed of 0.999 c 
#as percieved as a passenger on the ship is:  0.4475 years
