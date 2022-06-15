"""
Description: this ufnction recusrively reverses a list
Date Created/Last Modified: 11/2
Original Author: Rahul Arora
"""


#importing
import checkmycode

#defining function
def reverse(l):

   #base case
   if len(l) == 0:
      return []

   #returning last thing in list- converted to list, plus reversed beginning of list
   return [ l[len(l)-1]] + reverse(l[0:len(l)-1])



