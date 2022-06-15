import checkmycode
import time
import random

#writing test functions
def test(alist, i):
    #return value at index, i
     return  alist[i]
    
#--TESTING
for num in range(10):
    #looping through 1000-10000
    size = (num+1)*1000
    listOfSize = []

    #fill  nums in list
    for s in range(size):
        listOfSize.append(0)

    #starting time
    start_time = time.time()

    randex = random.randrange(0,size)
    test(listOfSize, randex)
    #checking time, printing results
    print("Size: " +  str(size) + ", Returned: " + str(randex) + ", Time: " + str(time.time() - start_time))


