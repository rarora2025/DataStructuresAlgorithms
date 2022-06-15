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

def testMyTree(thingToTest):
  dataType = "BinaryTree"
  print ("----------------------")
  print ("--- Starting Point ---")
  print ("----------------------")
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(len(thingToTest), 0)
  print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
  testfunction(thingToTest.is_empty(), True)
  print ("----------------------")
  print ("---- insert ------")
  print ("----------------------")
  item = 6
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6]")
  print ("----------------------")
  item = 2
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2]")
  print ("----------------------")
  item = 3
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3]")
  print ("----------------------")
  item = 10
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10]")
  print ("----------------------")
  item = 7
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10, 7]")
  print ("----------------------")
  item = 4
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10, 7, 4]")
  print ("----------------------")
  item = 5
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10, 7, 4, 5]")
  print ("----------------------")
  item = 1
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10, 7, 4, 5, 1]")
  print ("----------------------")
  item = 11
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 2, 3, 10, 7, 4, 5, 1, 11]")
  testfunction(len(thingToTest), 9)
  testfunction(thingToTest.is_empty(), False)

  print ("----------------------")
  print ("-- delete(item) --")
  print ("----------------------")
  item = 2
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 11, 3, 10, 7, 4, 5, 1]")
  print ("----------------------")
  item = 1
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[6, 11, 3, 10, 7, 4, 5]")
  print ("----------------------")
  item = 6
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[5, 11, 3, 10, 7, 4]")
  testfunction(len(thingToTest), 6)
  print ("----------------------")
  item = 1
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[5, 11, 3, 10, 7, 4]")
  testfunction(len(thingToTest), 6)
  testfunction(thingToTest.is_empty(), False)
  


def checkMyCode():
  # try:
  #   testMyTree(BinaryTree())
  # except NameError:
  #   print("")
  #   print("Error: Make sure you have all the methods you need, and that they are correctly named.")
  #   print("")
  # pass

  #If you are sure you have implemented all of the required functions, comment the try/except above and uncomment the code below.
  testMyTree(BinaryTree())

  
checkMyCode()