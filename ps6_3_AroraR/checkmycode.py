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

def testMyAVL(thingToTest):
  dataType = "AVLTree"
  print ("----------------------")
  print ("--- Starting Point ---")
  print ("----------------------")
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(len(thingToTest), 0)
  print ("%s is Empty? %s" % (dataType, thingToTest.is_empty()))
  testfunction(thingToTest.is_empty(), True)
  print ("----------------------")
  print ("---- insert(item) ------")
  print ("----------------------")
  item = 19
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 1)]")
  print ("----------------------")
  item = 107
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 2), (107, 1)]")
  print ("----------------------")
  item = 2
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 2), (2, 1), (107, 1)]")
  print ("----------------------")
  item = 1
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 3), (2, 2), (107, 1), (1, 1)]")
  print ("----------------------")
  item = 36
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 3), (2, 2), (107, 2), (1, 1), (36, 1)]")
  print ("----------------------")
  item = 108
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 3), (2, 2), (107, 2), (1, 1), (36, 1), (108, 1)]")
  print ("----------------------")
  item = 37
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 4), (2, 2), (107, 3), (1, 1), (36, 2), (108, 1), (37, 1)]")
  print ("----------------------")
  item = 34
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 4), (2, 2), (107, 3), (1, 1), (36, 2), (108, 1), (34, 1), (37, 1)]")
  print ("----------------------")
  item = 1
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 4), (2, 2), (107, 3), (1, 1), (36, 2), (108, 1), (34, 1), (37, 1)]")
  print ("----------------------")
  item = 11
  thingToTest.insert(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 4), (2, 2), (107, 3), (1, 1), (11, 1), (36, 2), (108, 1), (34, 1), (37, 1)]")
  testfunction(len(thingToTest), 9)
  testfunction(thingToTest.is_empty(), False)

  print ("----------------------")
  print ("-- find(item) --")
  print ("----------------------")
  item = 10
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), False)
  print ("----------------------")
  item = 45
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), False)
  print ("----------------------")
  item = 34
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), True)
  print ("----------------------")
  item = 1
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), True)
  print ("----------------------")
  item = 109
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), False)
  print ("----------------------")
  item = 19
  print ("Search for item: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(thingToTest.find(item), True)

  print ("----------------------")
  print ("-- delete(item) --")
  print ("----------------------")
  item = 2
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(19, 4), (11, 2), (107, 3), (1, 1), (36, 2), (108, 1), (34, 1), (37, 1)]")
  print ("----------------------")
  item = 1
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(36, 3), (19, 2), (107, 2), (11, 1), (34, 1), (37, 1), (108, 1)]")
  print ("----------------------")
  item = 6
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(36, 3), (19, 2), (107, 2), (11, 1), (34, 1), (37, 1), (108, 1)]")
  testfunction(len(thingToTest), 7)
  print ("----------------------")
  item = 36
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(37, 3), (19, 2), (107, 2), (11, 1), (34, 1), (108, 1)]")
  print ("----------------------")
  item = 107
  thingToTest.delete(item)
  print ("Item Added: %i" % item)
  print ("%s: %s" % (dataType, thingToTest))
  print ("%s size: %i" % (dataType, len(thingToTest)))
  testfunction(str(thingToTest), "[(37, 3), (19, 2), (108, 1), (11, 1), (34, 1)]")
  testfunction(len(thingToTest), 5)
  testfunction(thingToTest.is_empty(), False)
  

def checkMyCode():
  # try:
  #   testMyAVL(AVLTree())
  # except NameError:
  #   print("")
  #   print("Error: Make sure you have all the methods you need, and that they are correctly named.")
  #   print("")
  # pass

  #If you are sure you have implemented all of the required functions, comment the try/except above and uncomment the code below.
  testMyAVL(AVLTree())

  
checkMyCode()