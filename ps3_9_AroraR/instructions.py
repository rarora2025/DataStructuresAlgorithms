'''
Description:

Using a random number generator, create a list of 500 integers. Perform a benchmark analysis using 4 of the sorting algorithms from this chapter. What is the difference in execution speed?

There is no check my code, but your output should look like this:

Average BUBBLE Sort: #.########
Average SELECTION Sort: #.########
Average INSERTION Sort: #.########
Average SHELL Sort: #.########
Average MERGE Sort: #.########
Average QUICK Sort: #.########

Original Author: Rahul Arora
'''

#importing 
from random import random
from datetime import datetime

#defining insertion sort function
def insertionSort(alist):
    #looping through all indexes, excluding first
    for x in range(1,len(alist)):
        #key value
                   current = alist[x]

                   #index before
                   index = x-1

                   #while, still in list, and index before is greater than current, insert current before one preceding it
                   while index>0 and current < alist[index]:
                       alist[index+1] = alist[index]
                       index = index -1
                    #insert
                   alist[index+1] = current
                       

#defining selection sort
def selectionSort(array):

    #looping through each element
    for x in range(len(array)):
        
         #setting default for min index
        mindex = x
       

        #looping through rest of away
        for y in range(x, len(array)):
            #finding min index, assigning it to variable, mindex
            if(array[y] < array[mindex]):
                mindex = y
    #switiching current index and smallest avaiable inedx
        array[x], array[mindex] = array[mindex], array[x]


#defining shell sort
def shellSort(alist, inc=2):
    #while list exsists
    if len(alist) > 0:
        #making sure increment is valid
        if (inc <= 1 or inc > len(alist)):
            inc = 2
            #calculating number of "groups", seperated by gapsize/inc
        sublists = len(alist)//inc

        #while gapsize is greater than zero
        while sublists > 0:
            #call a gapsort on each sublist
            for startpos in range(sublists):
                gapsort(alist, startpos,sublists)
                
            #make number of sublists smaller
            sublists = sublists // inc
               
  
#define function to perform gapsort
def gapsort(alist,start,gap):
    #for each gap
    for i in range(start+gap,len(alist),gap):
#find current positions
        currentvalue = alist[i]
        position = i
#checking to see if previous value is greater or not, switching if needed
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

#define bubble sort
def bubbleSort(array):

    #repeating array times, for each element
    for x in range(len(array)-1):
        for y in range(len (array)-1):

            #checking to see if next element is greater, if so switch using simultaneous assignment
            if(array[y] > array[y+1]):
                array[y], array[y+1] = array[y+1], array[y]



#define checktime
def checkTime(func):

#defining start
    start=datetime.now()
    array = []
    for x in range(500):
        array.append(random())

    func(array)
    #seeing how much time has passed since start
    time = (datetime.now()-start)

    return  str(time)


#OUTPUT
print("Average BUBBLE Sort :  " + checkTime(bubbleSort))
print("Average SELECTION  Sort :  " + checkTime(selectionSort))
print("Average INSERTION Sort :  " + checkTime(insertionSort))
print("Average SHELL Sort :  " + checkTime(shellSort))


