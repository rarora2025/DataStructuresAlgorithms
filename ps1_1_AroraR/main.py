"""
Description: This program analyzes the runtime of an efficient function that finds the minimum value of a list.
Date Created/Last Modified: 10/18/2021
Original Author: Rahul Arora
"""

#imports
import checkmycode
import random
import time

#function findMin, returns lowest number taking parameter - list 'l'
def findMin(l):
    
    #default lowest value- first value in list
    lowest_of_all = l[0]

    #loop through all numbers find if current number is less than lowest; if so set lowest to current number
    for number in l:
        if (number < lowest_of_all):
            lowest_of_all = number
       
    #return lowest
    return lowest_of_all


#--TESTING
for num in range(10):
    #looping through 1000-10000
    size = (num+1)*1000
    listOfSize = []

    #fill random nums in list
    for s in range(size):
        listOfSize.append(random.randrange(0,100))

    #starting time
    start_time = time.time()
    #finding min
    findMin(listOfSize)
    #checking time, printing results
    print("Size: " +  str(size) + ", Time: " + str(time.time() - start_time))


