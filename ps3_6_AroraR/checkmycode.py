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

def oneInput(moduleName, testFunction,expectedOutput, testInput1, testInput2):
  try:
    package = moduleName
    name = testFunction
    with suppress_stdout():
      testedFunction = getattr(__import__(package, fromlist=[name]), name)
      actual = testedFunction(testInput1, testInput2)
      
      if expectedOutput != actual:
        raise UnexpectedOutput

  except UnexpectedOutput:
    print('........') 
    print('test input1: ',testInput1)
    print('test input2: ',testInput2)
    print('expected output: ',expectedOutput)
    print('actual output: ',actual)
    print('FAIL: Unexpected output. Check your algorithm...')
    
  else:
    print('........') 
    print('test input1: ',testInput1)
    print('test input2: ',testInput2)
    print('expected output: ',expectedOutput)
    print('actual output: ',actual)
    print('PASS: Everything looks good')

def checkCode(moduleName, testFunction, expectedOutput, testInput1, testInput2):
  expectedType = type(expectedOutput[0])
  if input != None:
    inputType1 = type(testInput1[0])
    inputType2 = type(testInput2[0])
  

  try:
    package = moduleName
    name = testFunction
    with suppress_stdout():
      testedFunction = getattr(__import__(package, fromlist=[name]), name)
      actual = testedFunction(testInput1[0],testInput2[0])

    if expectedType != type(actual):
        raise UnexpectedOutputType

  except NameError:
    print('FAIL : Your solution needs a function called','"'+testFunction + '"')
  except AttributeError:
    print('FAIL : Your solution needs a function called','"'+testFunction + '"')    
  except TypeError:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('FAIL : '+testFunction + '() should take two parameters of type '+str(inputType1) + " and "+ str(inputType2))
      
  except UnexpectedOutputType:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('PASS : '+testFunction + '() should take two parameters of type '+str(inputType1) + " and "+ str(inputType2))
    print('FAIL : '+testFunction + '() should return a value of type',expectedType)  
  else:
    print('PASS : Your solution needs a function called','"'+testFunction + '"')
    print('PASS : '+testFunction + '() should take two parameters of type '+str(inputType1) + " and "+ str(inputType2))
    print('PASS : '+testFunction + '() should return a value of type',expectedType)  

    for i in range(len(testInput1)):
      oneInput(moduleName, testFunction, expectedOutput[i], testInput1[i], testInput2[i]) 

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
  print("########## flex_insertion Sort ##########")
  print("")
  moduleName = 'main'
  testFunction = 'flex_insertion'

  input1 = [[13, 1903, 2, 1903, 0],[13, 1903, 2, 1903, 0],[1,243,83,654,35],[1,243,83,654,35],[4,4],[4,4],[309,21,51,34,105],[309,21,51,34,105], [], [],[2], [2],[2,1], [2,1]]
  input2 = ["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"]
  expectedOutput = [[0,2,13,1903, 1903],[1903,1903,13,2, 0],[1,35,83,243,654],[654,243,83,35,1],[4,4],[4,4],[21,34,51,105,309],[309,105,51,34,21],[],[],[2],[2],[1,2],[2,1]]

  print("About to run checkCode")
  checkCode(moduleName, testFunction, expectedOutput, input1, input2)
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