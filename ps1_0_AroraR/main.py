"""
Description: This program analyzes the runtime of an inefficient function that finds the minimum value of a list.
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

    #loop through all numbers- OUTER LOOP
    for number in range(0,len(l)):
        #generate default- first val in list
        lowest = l[number]

        #loop through inner, see if any prev number is lower. 
        for earlier_num in  range(0,number):
            if(l[earlier_num] < lowest):
                lowest = l[earlier_num]

    #see if lowest within that loop- up to this point ,is the overall lowest
        if(lowest < lowest_of_all):
             lowest_of_all = lowest
            
    return lowest_of_all


#TESTING
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
    print("Size " + str(num+1) + ": " +  str(size) + ", Time: " + str(time.time() - start_time))


