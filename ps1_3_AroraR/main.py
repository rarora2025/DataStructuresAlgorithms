"""
Description: This program has a function that finds the kth smallest integer of a list provided, using built in timsort (sort() ) with runtime complexity of O(n. logn).
Date Created/Last Modified:10/20
Original Author: Rahul Arora

"""
import checkmycode

def findK(a, b):
    
#The Python list sort(), uses Timsort algorithm. This algorithm has a runtime complexity of O(n. logn).
    a.sort()


    #getting kth smallest int since it is in sorted order now
    return a[b-1]



  

