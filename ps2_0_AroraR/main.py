"""
Description: this program recursively returns factorial
Original Author: Rahul Arora
"""


#importing
import checkmycode

#defining actual function
def factorial(y):
#base case
    if (y <= 1):
        return 1
        
        #calculating factorial
    return y * factorial(y-1)



