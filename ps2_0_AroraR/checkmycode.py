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
  test = testInput1
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
  print("########## Check My Code ##########")
  print("\tBEGIN TESTS")
  moduleName = 'main'
  testFunction = 'factorial'
  input1 = [0,1,5,12]
  expectedOutput = [1,1,120,479001600]
  checkCode(moduleName, testFunction, expectedOutput, input1)
  print("")
  print("###################################")
  print("\tALL TESTS COMPLETED")
checkMyCode()