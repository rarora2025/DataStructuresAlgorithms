from main import *

import importlib, sys, os
from contextlib import contextmanager

@contextmanager
def suppress_stdout():
  with open(os.devnull, "w") as devnull:
      old_stdout = sys.stdout
      sys.stdout = devnull
      try:  
          yield
      finally:
          sys.stdout = old_stdout

def testfunction(actualValue, expectedValue):
  if actualValue == expectedValue:
    print("PASS: " + "expected output matches actual")
  else:
    print("FAIL: Output does not match, check your algorithm. ")
    print("   -  Your output:     " + str(actualValue))
    print("   -  Expected output: " + str(expectedValue))

def testMyUnorderedList(thingToTest):
    dataType = 'UnorderedList'
    print ("----------------------")
    print ("--- Starting Point ---")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))

    print ("\r\n----------------------")
    print ("------- add() --------")
    print ("----------------------")
    item = 1
    thingToTest.add(1)
    print ("Item Added: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[1]")
    print ("----------------------")
    item = 4
    thingToTest.add(4)
    print ("Item Added: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[4, 1]")
    print ("----------------------")
    item = 3
    thingToTest.add(3)
    print ("Item Added: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[3, 4, 1]")
    print ("----------------------")
    item = 4
    thingToTest.add(4)
    print ("Item Added: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[4, 3, 4, 1]")

    print ("\r\n----------------------")
    print ("---- index(item) -----")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    item = 4
    print ("Index of item '%i': %s" % (item, thingToTest.index(item)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(thingToTest.index(item), 0)
    print ("----------------------")
    item = 3
    print ("Index of item '%i': %s" % (item, thingToTest.index(item)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(thingToTest.index(item), 1)
    print ("----------------------")
    item = 1
    print ("Index of item '%i': %s" % (item, thingToTest.index(item)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(thingToTest.index(item), 3)

    print ("\r\n----------------------")
    print ("------ remove() ------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    item = 10
    thingToTest.remove(10)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 3, 4, 1]")
    print ("----------------------")
    item = 1
    thingToTest.remove(1)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 3, 4]")
    print ("----------------------")
    item = 4
    thingToTest.remove(4)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[3, 4]")
    print ("----------------------")
    item = 3
    thingToTest.remove(3)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4]")
    print ("----------------------")
    item = 4
    thingToTest.remove(4)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[]")
    print ("----------------------")
    item = 10
    thingToTest.remove(10)
    print ("Item Removed: %i" % item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[]")

    print ("\r\n----------------------")
    print ("----- append() -------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    item = 2
    thingToTest.append(2)
    print ("Item Appended: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[2]")
    print ("----------------------")
    item = 3
    thingToTest.append(3)
    print ("Item Appended: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[2, 3]")
    print ("----------------------")
    item = 5
    thingToTest.append(5)
    print ("Item Appended: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[2, 3, 5]")
    print ("----------------------")
    item = 17
    thingToTest.append(17)
    print ("Item Appended: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[2, 3, 5, 17]")
    print ("----------------------")
    item = 5
    thingToTest.append(5)
    print ("Item Appended: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[2, 3, 5, 17, 5]")

    print ("\r\n----------------------")
    print ("------- pop() --------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    print ("Item Removed: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[3, 5, 17, 5]")
    print ("----------------------")
    print ("Item Removed: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[5, 17, 5]")
    print ("----------------------")
    print ("Item Removed: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[17, 5]")
    print ("----------------------")
    print ("Item Removed: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[5]")
    print ("----------------------")
    print ("Item Removed: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[]")

    print ("\r\n----------------------")
    print ("-- insert(pos, item) -")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    index = 0
    item = 4
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4]")
    print ("----------------------")
    index = 1
    item = 12
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 12]")
    print ("----------------------")
    index = 1
    item = 28
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 28, 12]")
    print ("----------------------")
    index = 3
    item = 50
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 28, 12, 50]")
    print ("----------------------")
    index = 1
    item = 12
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 12, 28, 12, 50]")
    testfunction(thingToTest.size(), 5)
    print ("----------------------")
    index = 1
    item = 60
    print ("Item index: %i" % index)
    print ("Item inserted: %i" % item)
    thingToTest.insert(index, item)
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 60, 12, 28, 12, 50]")

    print ("\r\n----------------------")
    print ("-- value_at(pos) -")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("----------------------")
    index = 0
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 4)
    print ("----------------------")
    index = 3
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 28)
    print ("----------------------")
    index = 1
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 60)
    print ("----------------------")
    index = 2
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 12)
    print ("----------------------")
    index = 4
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 12)
    print ("----------------------")
    index = 5
    print ("Item index: %i" % index)
    item = thingToTest.value_at(index)
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(item, 50)


    print ("\r\n----------------------")
    print ("----- pop(pos) -------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("----------------------")
    index = 4
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 60, 12, 28, 50]")
    print ("----------------------")
    index = 2
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 60, 28, 50]")
    print ("----------------------")
    index = 0
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[60, 28, 50]")
    print ("----------------------")
    index = 4
    print ("Item index: %i" % index)
    print ("Item Removed: %s" % str(thingToTest.pop(index)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[60, 28, 50]")
    testfunction(thingToTest.size(), 3)
    print ("----------------------")
    index = 1
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[60, 50]")
    print ("----------------------")
    index = 0
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[50]")
    print ("----------------------")
    index = 0
    print ("Item index: %i" % index)
    print ("Item Removed: %i" % thingToTest.pop(index))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[]")

def checkMyCode():
  try:
    testMyUnorderedList(UnorderedList())
  except NameError:
    print("")
    print("Error: Make sure you have all the methods you need, and that they are correctly named.")
    print("")
  pass
pass

checkMyCode()