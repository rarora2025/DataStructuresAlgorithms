#importing modules
import unicodedata
import random


#asking user for # points or if they want to quit
points =int( input("How many points? (Type 0 to QUIT): "))

while(points != 0):
    #creating new list to store points
    lister= []

#generating random points
    for x in range(points):
        point = (random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
        lister.append(point)

#var to hold number of points that fall within the circle
    points_in_cir = 0

#looping through to find if it falls in equation
    for z in lister:
    ##(x)2 + (y)2 <= 1 means that it falls in the circle
        if(z[0]**2 + z[1]**2 <= 1):
            points_in_cir += 1
        

#printing the points
    for xy in range(points):
        print("Point #" + str(xy+1) + ": " +str( lister[xy]))

#printing number that fall in the circle
    print("Number of Points that fall in circle: " + str(points_in_cir))

#printing estimation of PI
    print("According to your points and the Monte Carlo Method,  " + unicodedata.lookup("GREEK SMALL LETTER PI") + " = " + str((points_in_cir*4.0)/points))
    points =int( input("How many points? (Type 0 to QUIT): "))
