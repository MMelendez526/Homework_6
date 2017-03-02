#Altitude of a satellite
from math import pi
#Satellite to be launched in circular orbit around Earth so it orbits once 
#every T seconds
G = 6.67*10**-11
M = 5.97*10**24
R = 6371000
T = int(input("Enter the orbital period of the satellite (in seconds): "))


#Show that the altitude h above earth's surface that the satellite must have is
h = (((G*M*(T**2))/(4*pi*pi))**(1/3))-R
alt = int(round(h, 0)) #Doing this to round to the nearest whole number
print("The altitude of your satellite is: ", alt, "meters")

#Altitude of geosynchronous orbit: 35,855,910 meters
#Altitude of 90-minute orbit: 279,322 meters
#Altitude of 45-minute orbit: -2,181,560 meters
#This tells us that a 45-minute orbit is not possible, since the resulting
#orbit would be approximately 4189 kilometers below the surface of the earth

#A geosynchronous orbit is actually 23.93 hours, a persidereal day, this is 
#because one day on earth is not actually 24 hours, but the earth rotates once
#on its axis every 23.93 hours
#The difference in altitude between a persidereal day orbit and a 24 hour 
#orbit is 82,148 meters
