"""
Description: this function recusrively reverses a string
Date Created/Last Modified: 11/2
Original Author: Rahul Arora
"""

#defining function
def reverse(s):

    #base case
    if (len(s) == 0):
        return ""

    #algorithm to reverse- take last letter, bring it to front, add rest of string which same action will be performed on
    return s[-1] +reverse( s[:len(s)-1])

#TEST CASES:
print(reverse("pots&pans"))
print(reverse("hello"))
print(reverse("12345"))
print(reverse("racecar"))
