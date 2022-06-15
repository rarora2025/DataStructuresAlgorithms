'''
Implement the binary search using recursion without the slice operator. Recall that you will need to pass the list along with the starting and ending index values for the sublist. Generate random, ordered lists of integers, do a benchmark analysis, and explain.

Your output should look like this (replace brackets with text and hash tags with digits accordingly):

Average Bin Search Rec Slice Time: #.######## 
Average Bin Search Rec No Sl Time: #.########
Average Bin Search Iterative Time: #.########
Explanation: Average [choose Rec Slice/Rec No Sl/Iterative] is fastest because [insert your own reasoning]
You should have four functions:

binarySearchIt(alist, item)
binarySearchRec(alist, item)
binarySearchRecNoSl(alist, item)
checkTime(func) (you can pass a function as a parameter!)
Use import checkmycode to make sure you are on the right track.
'''


#imports
import checkmycode
from datetime import datetime
from random import random
#iterative binary search
def binarySearchIt(alist, item):

    left = 0
    right = len(alist) - 1

    while right >= left:

        mid = (left + right) //2

        if alist[mid] == item:
            return True

        elif alist[mid] < item:
            left = mid + 1

        else:
            right = mid - 1

    return False

#recursive binary search 
def binarySearchRec(alist, item):
    low = 0
    high = len(alist)-1
    if high >= low:
        mid = (high + low) // 2
    else:
        return False
 
    if alist[mid] == item:
        return True
 
    elif alist[mid] > item:
        return  binarySearchRec(alist[low:mid], item)
    else:
        return binarySearchRec(alist[mid + 1:high+1], item)
    
 
#recursive binary search 
def binarySearchRecNoSl(alist, item):
    def rec(array, low, high, x):
        if high >= low:
            mid = (high + low) // 2
        else:
            return False
 
        if array[mid] == x:
            return True
 
        elif array[mid] > x:
            return rec(array, low, mid - 1, x)
 
        else:
            return rec(array, mid + 1, high, x)
      
 

     
    return rec(alist, 0, len(alist)-1, item)

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

#printing output
print("Average Iterative Search Time: " + checkTime(binarySearchIt))
print("Average Recursive slice Search Time: " + checkTime(binarySearchRec))
print("Average Recursive No slice Search Time: " + checkTime(binarySearchRecNoSl))
print("Explanation:  Average [Iterative] search is slower because O(1) is more efficient than O(logn)")
