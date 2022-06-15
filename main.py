import random
import string
filer = open('word-list.txt', 'r')
lines = filer.readlines()

'''
for line in lines:
    print(line)
'''    
filer.close()

def returnBoggle():
    grid = []
    for i in range(5):
        mini_grid = []
        for j in range(5):
            mini_grid.append(random.choice(string.ascii_letters).lower())
        grid.append(mini_grid)
    return grid

def printBoggle(boggleToPrint):
    for line in boggleToPrint:
        print(line)
    
def getRowCombos(rows, cur_words, grid):
   # print(grid)
   
    if(rows == -1):
        return cur_words

    #all combos
    cur_words.append(grid[rows][0:3])
    cur_words.append(grid[rows][1:4])
    cur_words.append(grid[rows][2:5])
    cur_words.append(grid[rows][0:4])
    cur_words.append(grid[rows][1:5])
    cur_words.append(grid[rows][0:5])
    
    return getRowCombos(rows-1, cur_words, grid)

#print(returnBoggle())


def switchColsAndRows(array2d):
    new_grid = []
    for x in range(5):
        new = []
        for y in range (5):
            new.append(array2d[y][x])
        new_grid.append(new)
    return new_grid

'''
print("TESTING SWITCH.......")
gridder = returnBoggle()
print(gridder)
print(switchColsAndRows(gridder))
'''



def makeArrayToWord(array):
    output = ""
    for letter in array:
        output += letter
    return output


def getDiagonalArrays(bogglefive):
    diag = []
    mini = []

    #getting large diagonals
    for x in range(5):
        mini.append(bogglefive[x][x])

    diag.append(mini)

    mini = []
    for x in range(5):
        mini.append(bogglefive[x][4-x])
            
    diag.append(mini)
    mini = []
    
    #getting 4 letter diagonals
    for x in range(4):
        mini.append(bogglefive[x][x+1])
    diag.append(mini)
    
    mini = []
    for x in range(4):
        mini.append(bogglefive[x+1][x])
    diag.append(mini)

    mini = []
    for x in range(4):
        mini.append(bogglefive[x][3-x])
    diag.append(mini)

    mini = []
    for x in range(4):
        mini.append(bogglefive[x+1][4-x])
    diag.append(mini)


    mini = []
    for x in range(3):
        mini.append(bogglefive[x+2][x])
    diag.append(mini)

    mini = []
    for x in range(3):
        mini.append(bogglefive[x][x+2])
    diag.append(mini)

    mini = []
    for x in range(3):
        mini.append(bogglefive[x+2][4-x])
    diag.append(mini)

    mini = []
    for x in range(3):
        mini.append(bogglefive[x][2-x])
    diag.append(mini)

    return diag

    

    


    
#getting ALL POSSIBILITES, rows, columns, and diagonals are added and checked
x  = returnBoggle()
printBoggle(x)
x = x +  switchColsAndRows(x)
diags =  getDiagonalArrays(x)
x = x + [diags[0]]
x = x + [diags[1]]
combos = getRowCombos(len(x)-1, [], x)

combos +=  [diags[-1]]
combos +=  [diags[-2]]
combos +=  [diags[-3]]
combos +=  [diags[-4]]

for x in range(4):
    combos += [diags[x+2]]
    combos += [diags[x+2][0:3]]
    combos += [diags[x+2][1:4]]

combosInString = []
#printing all combination
for combo in combos:
    combosInString.append(makeArrayToWord(combo))

#COMBOS IN STRING HAS ALL POSSIBLE COMBOS NOT CRISS CROSS

truth = []
def filterWords(arrayOfPossibilites):
    for word in lines:

        for pos in arrayOfPossibilites:
            print(pos)
            if(pos.strip() == word.strip()):
                truth.append(pos)
                print(pos)
                continue

filterWords(combosInString)

print(truth)
                
        
        
