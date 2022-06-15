'''
Implement the bubble sort using simultaneous assignment.

Use import checkmycode to make sure you are on the right track.

'''

#import
import checkmycode

#defining function
def bubbleSort(array):

    #repeating array times, for each element
    for x in range(len(array)-1):
        for y in range(len (array)-1):

            #checking to see if next element is greater, if so switch using simultaneous assignment
            if(array[y] > array[y+1]):
                array[y], array[y+1] = array[y+1], array[y]

#return result
    return  array



