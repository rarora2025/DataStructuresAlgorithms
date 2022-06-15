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

def testMyULStack(thingToTest):
    dataType = 'Stack'
    print ("----------------------")
    print ("--- Starting Point ---")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(thingToTest.size(), 0)
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    testfunction(thingToTest.is_empty(), True)
    print ("----------------------")
    print ("------ push() --------")
    print ("----------------------")
    item = 1
    thingToTest.push(1)
    print ("Item Pushed: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[1]")
    print ("----------------------")
    item = 4
    thingToTest.push(4)
    print ("Item Pushed: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[4, 1]")
    print ("----------------------")
    item = 27
    thingToTest.push(27)
    print ("Item Pushed: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[27, 4, 1]")
    print ("----------------------")
    item = 3
    thingToTest.push(3)
    print ("Item Pushed: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[3, 27, 4, 1]")
    print ("----------------------")
    item = 4
    thingToTest.push(4)
    print ("Item Pushed: %i" % item)
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s size: %i" % (dataType, thingToTest.size()))
    testfunction(str(thingToTest), "[4, 3, 27, 4, 1]")
    testfunction(thingToTest.size(), 5)

    print ("----------------------")
    print ("----------------------")
    print ("------- pop() --------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
    testfunction(thingToTest.is_empty(), False)
    print ("----------------------")
    print ("%s peek: %i" % (dataType, thingToTest.peek()))
    print ("Item Popped: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[3, 27, 4, 1]")
    print ("----------------------")
    print ("%s peek: %i" % (dataType, thingToTest.peek()))
    print ("Item Popped: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[27, 4, 1]")
    print ("----------------------")
    print ("%s peek: %i" % (dataType, thingToTest.peek()))
    print ("Item Popped: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[4, 1]")
    print ("----------------------")
    print ("%s peek: %i" % (dataType, thingToTest.peek()))
    print ("Item Popped: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[1]")
    print ("----------------------")
    print ("%s peek: %i" % (dataType, thingToTest.peek()))
    print ("Item Popped: %i" % thingToTest.pop())
    print ("%s size: %i" % (dataType, thingToTest.size()))
    print ("%s: %s" % (dataType, str(thingToTest)))
    testfunction(str(thingToTest), "[]")
    testfunction(thingToTest.size(), 0)

def checkMyCode():
  try:
    testMyULStack(ListStack())
  except NameError:
    print("")
    print("Error: Make sure you have all the methods you need, and that they are correctly named.")
    print("")

checkMyCode()