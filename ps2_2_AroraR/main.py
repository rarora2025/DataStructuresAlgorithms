"""
Description: this function does the fibonacci sequence recursively
Date Created/Last Modified: 11/2
Original Author: Rahul Arora

How does the performance of the recursive function compare to that of an iterative version?
For the fibonacci example, the iterative version has time performance O(n), whereas the recursive has performance: O(2^n)


"""

#IMPORT check my code
import checkmycode

#define function
def fibonacci(x):

    #base cases
    if(x<=0):
        return 0
    elif (x <= 2):
        return 1
  

    #calculating number
    return fibonacci(x-1) + fibonacci(x-2)


