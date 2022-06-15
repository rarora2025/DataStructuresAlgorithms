
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

def oneInput(moduleName, testFunction,expectedOutput, testInput1):
  test = testInput1.copy()
  try:
    package = moduleName
    name = testFunction
    with suppress_stdout():
      testedFunction = getattr(__import__(package, fromlist=[name]), name)
      actual = testedFunction(testInput1)
      
      if expectedOutput != actual:
        raise UnexpectedOutput

  except UnexpectedOutput:
    print('........') 
    print('test input1: ',test)
    print('expected output: ',expectedOutput)
    print('actual output: ',actual)
    print('FAIL: Unexpected output. Check your algorithm...')
    
    
  else:
    print('........') 
    print('test input1: ',test)
    print('expected output: ',expectedOutput)
    print('actual output: ',actual)
    print('PASS: Everything looks good')
    

def checkCode(moduleName, testFunction, expectedOutput, testInput1):
  expectedType = type(expectedOutput[0])
  if input != None:
    inputType1 = type(testInput1[0])
    
  try:
    package = moduleName
    name = testFunction
    with suppress_stdout():
      testedFunction = getattr(__import__(package, fromlist=[name]), name)
      actual = testedFunction(testInput1[0])

    if expectedType != type(actual):
        raise UnexpectedOutputType

  except NameError:
    print('FAIL : Your solution needs a function called','"'+testFunction + '"')
  except AttributeError:
    print('FAIL : Your solution needs a function called','"'+testFunction + '"')    
  except TypeError:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('FAIL : '+testFunction + '() should take one parameter of type '+str(inputType1))
      
  except UnexpectedOutputType:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('PASS : '+testFunction + '() should take one parameter of type '+str(inputType1))
    print('FAIL : '+testFunction + '() should return a value of type',expectedType)  
  else:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('PASS : '+testFunction + '() should take one parameter of type '+str(inputType1))
    print('PASS : '+testFunction + '() should return a value of type',expectedType)  

    for i in range(len(testInput1)):
      oneInput(moduleName, testFunction, expectedOutput[i], testInput1[i]) 

class Error(Exception):
  """Base class for other exceptions"""
  pass

class UnexpectedOutput(Error):
  """Raised when the output is unexpected"""
  pass

class UnexpectedOutputType(Error):
  """Raised when the output is unexpected"""
  pass

def checkMyCode():
  print("")
  print ("############################")
  print ("##                        ##")
  print ("##   CHECKMYCODE OUTPUT   ##")
  print ("##                        ##")
  print ("############################")
  print("")
  print ("##  Selection SimulAssign ##")
  print("")
  
  moduleName = 'main'
  testFunction = 'selectionSort'
  input1 = [[13, 1903, 2, 1903, 0],[1,243,83,654,35],[4,4],[309,21,51,34,105],[],[2],[2,1]]
  expectedOutput = [[0,2,13,1903, 1903],[1,35,83,243,654],[4,4],[21,34,51,105,309],[],[2],[1,2]]
  checkCode(moduleName, testFunction, expectedOutput, input1)
  print("")
  print ()
  print ("############################")
  print ("##                        ##")
  print ("##    END CHECKMYCODE     ##")
  print ("##                        ##")
  print ("############################")
  print ()
  print("")
checkMyCode()