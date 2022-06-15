"""
Description:
Implement a radix sorting machine.
A radix sort for base 10 integers is a mechanical sorting technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts like a queue and maintains its values in the order that they arrive.

The algorithm begins by placing each number in the main bin.

Then it considers each value digit by digit.

The first value is removed and placed in a digit bin corresponding to the digit being considered. For example, if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7.

Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 and placed back in the main bin.

The process continues with the tens digit, the hundreds, and so on. After the last digit is processed, the main bin contains the values in order.

Use import checkmycode to check your code.

If you are like me and need a visualization to supplement the text heavy radix sort description, please try watching this video:
https://youtu.be/YXFI4osELGU

Original Author: Rahul Arora
"""
import checkmycode
#function to calculate number of digits, parameter is going to be the max number of array to determine iterations of bucket sorts
def calcDigs(maxi):
    #variable to hold number of digits
    digs = 0

    #keep dividing by 10 and adding to counter until less than 1
    while(int(maxi)>1):
        digs = digs + 1
        maxi /=10

    #return var holding number of digits
    return digs

#function to sort into bucket, given number of places (and list)
def getBucket(alist, places):
    #template
    bucket = [[],[],[],[],[],[],[],[],[],[]]

    #for each number in the list
    for number in alist:

# if leading zero 
        if number < (10**(places-1)):
            current = 0
        else:

            #finding current digit
            current = (number%((10**places)))/10**(places-1)

            #adding to pucket appropraitely
        bucket[int(current)].append(number)

#return bucket
    return bucket

#converting bucket of buckets to one single array
def bucketToArray(bucket):
    array = []
    #just going through list and adding to array
    for buck in bucket:
        for b in buck:
            array.append(b)
    return array

         # main function   
def radix(alist):
    maxi = alist[0]

#calling bucket sort, max places number of time 
    for y in alist:
        if y > maxi:
            maxi = y

    
    for z in range (1,maxi+1):
        #call
        alist = bucketToArray(getBucket(alist, z))

        #returning final list
    return alist

   

    
