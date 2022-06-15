'''
Implement the selection sort using simultaneous assignment.

Use import checkmycode to make sure you are on the right track.
'''

#importing check
import checkmycode

#defiining
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
    return array 
