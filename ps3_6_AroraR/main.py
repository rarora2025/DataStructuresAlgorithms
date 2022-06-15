"""
Description:a function, flex_insertion, that implements the insertion sorting algorithm.It takes two parameters, a list and + or - sign to designate direction, and returns the sorted list.
Original Author: Rahul Arora
"""
import checkmycode

#defining the function
def flex_insertion(array, sign):

    #evaluating parameter to see if should sort ascending or descending
    if (sign == "+"):
        #repeating for each index
        for y in range(0, len(array)):
            #keeping track of the current index
            curdex = y
            #comparing current index, to the index below it, it it is lower then switch the two 
            while curdex > 0 and array[curdex] < array[curdex-1]:
                array[curdex-1], array[curdex] = array[curdex], array[curdex-1]
            
                curdex = curdex-1
    elif (sign == "-"):
            #repeating for each index
        for y in range( 0, len(array)):
              #keeping track of the current index
            curdex = y
 #comparing current index, to the index below it, it it is higher then switch the two 
            while curdex > 0 and array[curdex] > array[curdex-1]:
                array[curdex-1], array[curdex] = array[curdex], array[curdex-1]
                curdex = curdex-1

 #returning modified array
    return array


