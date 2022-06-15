'''
Author: Rahul Arora
Descrpition:
Set up a random experiment to test the difference between a sequential search and a binary search on a list of integers.

Your output should look like this (replace hash tags with digits accordingly):

Average Bin Search Time: #.########
Average Seq Search Time: #.########
You should have three functions:

orderedSequentialSearch(alist, item)
binarySearch(alist, item)
checkTime(func) (you can pass a function as a parameter!)

Use import checkmycode to make sure you are on the right track.
'''
#imports
import checkmycode
from datetime import datetime
from random import random

#defining ordered sequential
def orderedSequentialSearch(alist, item):
    index = False
    for x in range(len(alist)):
        if alist[x] == item:
            index = True

    return index

#binary search
def binarySearch(alist, item):
    left = 0
    right = len(alist) - 1
    while right >= left:
        mid = (left + right) //2

        if alist[mid] == item:
            return True

        elif alist[mid] <item:
            left = mid + 1

        else:
            right = mid - 1

    return False

    #checking time 
def checkTime(func):
    #defining start1
    start1=datetime.now()
    array1 = []
    for x in range(5):
        array1.append(random)
    target1 = array1[len(array1)//2]
    func(array1, target1)
    #seeing how much time has passed for start1
    time1 = (datetime.now()-start1)

        #defining start2
    start2=datetime.now()
    array2 = []
    for x in range(100):
        array2.append(random)
    target2 = array2[len(array2)//2]
    func(array2, target2)
    #seeing how much time has passed for start2
    time2 = (datetime.now()-start2)

            #defining start3
    start3=datetime.now()
    array3 = []
    for x in range(1000):
        array3.append(random)
    target3 = array3[len(array3)//2]
    func(array3, target3)
    #seeing how much time has passed for start3
    time3 = (datetime.now()-start3)

                #defining start4
    start4=datetime.now()
    array4 = []
    for x in range(10000):
        array4.append(random)
    target4 = array4[len(array4)//2]
    func(array4, target4)
    #seeing how much time has passed for start4
    time4 = (datetime.now()-start4)

    return  str((time1+time2+time3+time4) / 4)
    

    #output
print("Average Bin Search Time: " + checkTime(binarySearch))
print("Average Seq Search Time: " + checkTime(orderedSequentialSearch))
