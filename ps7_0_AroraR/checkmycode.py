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
    print("\tPASS: " + "expected output matches actual")
  else:
    print("\tFAIL: Output does not match, check your algorithm. ")
    print("\t   -  Your output:     " + str(actualValue))
    print("\t   -  Expected output: " + str(expectedValue))

def testMySortedMap(thingToTest):
    dataType = 'SortedMap'
    print ("----------------------")
    print ("--- Starting Point ---")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s length: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print ("------- M[k] = v --------")
    print ("----------------------")
    print("")
    value = 45
    key = "france"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(france : 45)}")
    testfunction(str(len(thingToTest)), "1")
    print("")
    value = 20
    key = "spain"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(france : 45), (spain : 20)}")
    testfunction(str(len(thingToTest)), "2")
    print("")
    value = 60
    key = "mexico"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(france : 45), (mexico : 60), (spain : 20)}")
    testfunction(str(len(thingToTest)), "3")
    print("")
    value = 30
    key = "germany"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(france : 45), (germany : 30), (mexico : 60), (spain : 20)}")
    testfunction(str(len(thingToTest)), "4")
    print("")
    value = 75
    key = "america"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(america : 75), (france : 45), (germany : 30), (mexico : 60), (spain : 20)}")
    testfunction(str(len(thingToTest)), "5")
    print("")
    value = 10
    key = "russia"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(america : 75), (france : 45), (germany : 30), (mexico : 60), (russia : 10), (spain : 20)}")
    testfunction(str(len(thingToTest)), "6")
    print("")
    value = 100
    key = "america"
    thingToTest[key] = value
    print ("Adding Entry\r\nM[\"%s\"] = %i" % (key, value))
    testfunction(str(thingToTest), "{(america : 100), (france : 45), (germany : 30), (mexico : 60), (russia : 10), (spain : 20)}")
    testfunction(str(len(thingToTest)), "6")
    print("")
    
    print ("----------------------")
    print ("---- M[k] -----")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    key = "russia"
    print ("%s: M[\"%s\"] = %s" % (dataType, key, str(thingToTest[key])))
    testfunction(str(thingToTest[key]), "10")
    print("")
    key = "germany"
    print ("%s: M[\"%s\"] = %s" % (dataType, key, str(thingToTest[key])))
    testfunction(str(thingToTest[key]), "30")
    print("")
    key = "switzerland"
    print ("%s: M[\"%s\"] = %s" % (dataType, key, str(thingToTest[key])))
    testfunction(str(thingToTest[key]), "None")
    print("")
    key = "spain"
    print ("%s: M[\"%s\"] = %s" % (dataType, key, str(thingToTest[key])))
    testfunction(str(thingToTest[key]), "20")
    print("")

    print ("----------------------")
    print ("------ del M[k] ------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print("")
    key = "germany"
    del thingToTest[key]
    print ("Entry Deleted: M[\"%s\"]" % (key))
    testfunction(str(thingToTest), "{(america : 100), (france : 45), (mexico : 60), (russia : 10), (spain : 20)}")
    testfunction(str(len(thingToTest)), "5")
    print("")
    key = "spain"
    del thingToTest[key]
    print ("Entry Deleted: M[\"%s\"]" % (key))
    testfunction(str(thingToTest), "{(america : 100), (france : 45), (mexico : 60), (russia : 10)}")
    testfunction(str(len(thingToTest)), "4")
    print("")
    key = "russia"
    del thingToTest[key]
    print ("Entry Deleted: M[\"%s\"]" % (key))
    testfunction(str(thingToTest), "{(america : 100), (france : 45), (mexico : 60)}")
    testfunction(str(len(thingToTest)), "3")
    print("")
    key = "switzerland"
    del thingToTest[key]
    print ("Entry Deleted: M[\"%s\"]" % (key))
    testfunction(str(thingToTest), "{(america : 100), (france : 45), (mexico : 60)}")
    testfunction(str(len(thingToTest)), "3")
    print ("")
    
    print ("----------------------")
    print ("----- k in M -------")
    print ("----------------------")
    print ("Starting %s: %s" % (dataType, str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print ("")
    key = "france"
    act = key in thingToTest
    print("\"%s\" in M: %s" % (key, str(act)))
    testfunction(str(act), "True")
    print ("")
    key = "switzerland"
    act = key in thingToTest
    print("\"%s\" in M: %s" % (key, str(act)))
    testfunction(str(act), "False")
    print ("")
    key = "russia"
    act = key in thingToTest
    print("\"%s\" in M: %s" % (key, str(act)))
    testfunction(str(act), "False")
    print ("")
    key = "america"
    act = key in thingToTest
    print("\"%s\" in M: %s" % (key, str(act)))
    testfunction(str(act), "True")
    print ("")
    
    print ("----------------------")
    print ("------- set(k, v) --------")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s length: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print("")
    value = 50
    key = "france"
    s = ""
    try:
        thingToTest.set(key, value)
        s = str(thingToTest)
        print ("Entry Updated: (%s : %i)" % (key, value))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "{(america : 100), (france : 50), (mexico : 60)}")
    print("")
    value = 45
    key = "russia"
    s = ""
    try:
        thingToTest.set(key, value)
        s = str(thingToTest)
        print ("Entry Updated: (%s : %i)" % (key, value))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "'Error: Key russia not found in map'")

    print("")
    value = 25
    key = "germany"
    s = ""
    try:
        thingToTest.set(key, value)
        s = str(thingToTest)
        print ("Entry Updated: (%s : %i)" % (key, value))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "'Error: Key germany not found in map'")
    print("")
    value = 95
    key = "america"
    s = ""
    try:
        thingToTest.set(key, value)
        s = str(thingToTest)
        print ("Entry Updated: (%s : %i)" % (key, value))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "{(america : 95), (france : 50), (mexico : 60)}")
    print("")

    print ("----------------------")
    print ("------- get(k) --------")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s length: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print("")
    key = "france"
    s = ""
    try:
    	s = str(thingToTest.get(key))
    	print ("%s: M.get(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "50")
    print("")
    key = "russia"
    s = ""
    try:
    	s = str(thingToTest.get(key))
    	print ("%s: M.get(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "'Error: Key russia not found in map'")
    print("")
    key = "germany"
    s = ""
    try:
    	s = str(thingToTest.get(key))
    	print ("%s: M.get(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "'Error: Key germany not found in map'")
    print("")
    key = "america"
    s = ""
    try:
    	s = str(thingToTest.get(key))
    	print ("%s: M.get(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "95")
    print("")

    print ("----------------------")
    print ("------- pop(key) --------")
    print ("----------------------")
    print ("%s: %s" % (dataType, str(thingToTest)))
    print ("%s length: %i" % (dataType, len(thingToTest)))
    print ("----------------------")
    print("")
    key = "america"
    s = ""
    try:
    	s = str(thingToTest.pop(key))
    	print ("%s: M.pop(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "95")
    testfunction(str(thingToTest), "{(france : 50), (mexico : 60)}")
    testfunction(len(thingToTest), 2)
    print("")
    key = "france"
    s = ""
    try:
    	s = str(thingToTest.pop(key))
    	print ("%s: M.pop(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "50")
    testfunction(str(thingToTest), "{(mexico : 60)}")
    testfunction(len(thingToTest), 1)
    print("")
    key = "america"
    s = ""
    try:
    	s = str(thingToTest.pop(key))
    	print ("%s: M.pop(%s) = %s" % (dataType, key, s))
    except KeyError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "'Error: Key america not found in map'")
    testfunction(str(thingToTest), "{(mexico : 60)}")
    testfunction(len(thingToTest), 1)
    print("")

    thingToTest["france"] = 45
    thingToTest["spain"] = 60
    print ("----------------------")
    print ("----- popitem() -------")
    print ("----------------------")
    print ("Starting point: %s" % (str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    s = ""
    try:
    	s = str(thingToTest.popitem())
    	print ("%s: M.popitem() = %s" % (dataType, s))
    except IndexError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "(\'france\', 45)")
    testfunction(str(thingToTest), "{(mexico : 60), (spain : 60)}")
    testfunction(len(thingToTest), 2)
    print("")
    s = ""
    try:
    	s = str(thingToTest.popitem())
    	print ("%s: M.popitem() = %s" % (dataType, s))
    except IndexError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "(\'mexico\', 60)")
    testfunction(str(thingToTest), "{(spain : 60)}")
    testfunction(len(thingToTest), 1)
    print("")
    s = ""
    try:
    	s = str(thingToTest.popitem())
    	print ("%s: M.popitem() = %s" % (dataType, s))
    except IndexError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "(\'spain\', 60)")
    testfunction(str(thingToTest), "{}")
    testfunction(len(thingToTest), 0)
    print("")
    s = ""
    try:
    	s = str(thingToTest.popitem())
    	print ("%s: M.popitem() = %s" % (dataType, s))
    except IndexError as e:
    	s = str(e)
    	print(e)
    pass
    testfunction(s, "Error: Map has no entries")
    testfunction(str(thingToTest), "{}")
    testfunction(len(thingToTest), 0)
    print("")

    thingToTest["france"] = 45
    thingToTest["spain"] = 60
    thingToTest["america"] = 78
    thingToTest["mexico"] = 66
    thingToTest["egypt"] = 40
    thingToTest["canada"] = 55

    print ("----------------------")
    print ("----- clear() -------")
    print ("----------------------")
    print ("Starting point: %s" % (str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    thingToTest.clear()
    testfunction(str(thingToTest), "{}")
    testfunction(len(thingToTest), 0)
    print("")

    thingToTest["france"] = 45
    thingToTest["spain"] = 60
    thingToTest["america"] = 78
    thingToTest["mexico"] = 66
    thingToTest["egypt"] = 40
    thingToTest["canada"] = 55

    print ("----------------------")
    print ("----- keys() -------")
    print ("----------------------")
    print ("Starting point: %s" % (str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    testfunction(str(thingToTest.keys()), "[\'america\', \'canada\', \'egypt\', \'france\', \'mexico\', \'spain\']")
    print("")

    print ("----------------------")
    print ("----- values() -------")
    print ("----------------------")
    print ("Starting point: %s" % (str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    testfunction(str(thingToTest.values()), "[78, 55, 40, 45, 66, 60]")
    print("")

    print ("----------------------")
    print ("----- items() -------")
    print ("----------------------")
    print ("Starting point: %s" % (str(thingToTest)))
    print ("%s len: %i" % (dataType, len(thingToTest)))
    testfunction(str(thingToTest.items()), "[(\'america\', 78), (\'canada\', 55), (\'egypt\', 40), (\'france\', 45), (\'mexico\', 66), (\'spain\', 60)]")
    print("")

    otherMap = SortedMap()
    otherMap["america"] = 100
    otherMap["haiti"] = 65
    otherMap["jamaica"] = 70
    otherMap["barbados"] = 80
    otherMap["france"] = 15
    
    print ("----------------------")
    print ("----- M.merge(M2) -------")
    print ("----------------------")
    print ("--------------Before Merge--------------")
    print ("M1: %s" % (str(thingToTest)))
    print ("M2: %s" % (str(otherMap)))
    latestMap = thingToTest.merge(otherMap)
    print ("--------------After Merge--------------")
    testfunction(str(thingToTest), "{(america : 78), (canada : 55), (egypt : 40), (france : 45), (mexico : 66), (spain : 60)}")
    testfunction(str(otherMap), "{(america : 100), (barbados : 80), (france : 15), (haiti : 65), (jamaica : 70)}")
    testfunction(str(latestMap), "{(america : 78), (barbados : 80), (canada : 55), (egypt : 40), (france : 45), (haiti : 65), (jamaica : 70), (mexico : 66), (spain : 60)}")
    print("")

    thingToTest.clear()
    otherMap.clear()
    latestMap.clear()

    thingToTest[5] = "awesome"
    thingToTest[6] = "xylo"
    thingToTest[10] = "extreme"
    thingToTest[1] = "coffee"
    otherMap[15] = "car"
    otherMap[55] = "school"
    otherMap[10] = "tea"
    otherMap[2] = "band"
    print ("--------------Before Merge--------------")
    print ("M1: %s" % (str(thingToTest)))
    print ("M2: %s" % (str(otherMap)))
    latestMap = thingToTest.merge(otherMap)
    print ("--------------After Merge--------------")
    testfunction(str(thingToTest), "{(1 : coffee), (5 : awesome), (6 : xylo), (10 : extreme)}")
    testfunction(str(otherMap), "{(2 : band), (10 : tea), (15 : car), (55 : school)}")
    testfunction(str(latestMap), "{(1 : coffee), (2 : band), (5 : awesome), (6 : xylo), (10 : extreme), (15 : car), (55 : school)}")
    print("")

def checkMyCode():
  try:
    testMySortedMap(SortedMap())
  except NameError:
    print("")
    print("Error: Make sure you have all the methods you need, and that they are correctly named.")
    print("")

checkMyCode()