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

def testMyQueue(thingToTest):
  dataType = 'Queue'
  print ("----------------------")
  print ("--- Starting Point ---")
  print ("----------------------")
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(thingToTest.size(), 0)
  print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
  testfunction(thingToTest.is_empty(), True)
  print ("----------------------")
  print ("----- enqueue() ------")
  print ("----------------------")
  item = 7
  thingToTest.enqueue(7)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7]")
  print ("----------------------")
  item = 45
  thingToTest.enqueue(45)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7, 45]")
  print ("----------------------")
  item = 13
  thingToTest.enqueue(13)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7, 45, 13]")
  print ("----------------------")
  item = 150
  thingToTest.enqueue(150)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7, 45, 13, 150]")
  print ("----------------------")
  item = 7
  thingToTest.enqueue(7)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7, 45, 13, 150, 7]")
  testfunction(thingToTest.size(), 5)

  print ("----------------------")
  print ("----- dequeue() ------")
  print ("----------------------")
  print ("Starting %s: %s" % (dataType, thingToTest))
  print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
  testfunction(thingToTest.is_empty(), False)
  print ("----------------------")
  print ("Item Removed: %i" % thingToTest.dequeue())
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[45, 13, 150, 7]")
  print ("----------------------")
  print ("Item Removed: %i" % thingToTest.dequeue())
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[13, 150, 7]")
  print ("----------------------")
  print ("Item Removed: %i" % thingToTest.dequeue())
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[150, 7]")
  print ("----------------------")
  print ("Item Removed: %i" % thingToTest.dequeue())
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[7]")
  print ("----------------------")
  print ("Item Removed: %i" % thingToTest.dequeue())
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, thingToTest.size()))
  testfunction(str(thingToTest), "[]")
  testfunction(thingToTest.size(), 0)
  print ("----------------------")

def checkMyCode():
  try:
    testMyQueue(Queue())
  except NameError:
    print("")
    print("Error: Make sure you have all the methods you need, and that they are correctly named.")
    print("")

checkMyCode()