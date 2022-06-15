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
  item = 7
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[7]")
  print ("----------------------")
  item = 45
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[7, 45]")
  print ("----------------------")
  item = 13
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[7, 45, 13]")
  print ("----------------------")
  item = 150
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[7, 45, 13, 150]")
  print ("----------------------")
  item = 7
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[7, 45, 13, 150, 7]")
  testfunction(len(thingToTest), 5)
  testfunction(thingToTest.is_empty(), False)

  print ("----------------------")
  print ("-- Breadth-First Search() --")
  print ("----------------------")
  item = 10
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.breadth_search(item), False)
  print ("----------------------")
  item = 45
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.breadth_search(item), True)
  print ("----------------------")
  item = 150
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.breadth_search(item), True)
  print ("----------------------")
  item = 12
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.breadth_search(item), False)

  print ("----------------------")
  print ("-- Depth-First Search() --")
  print ("----------------------")
  item = 10
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.depth_search(item), False)
  print ("----------------------")
  item = 45
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.depth_search(item), True)
  print ("----------------------")
  item = 150
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.depth_search(item), True)
  print ("----------------------")
  item = 12
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.depth_search(item), False)
  


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