'''
Implement the AVL Tree we discussed in class. There is no checkmycode for this problem set, so be sure to thoroughly test your code.
Rahul Arora
5/22/2022 
'''

#base node class
class Node:
    def __init__(self, data):
        #basic attributes
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0

#AVL TREE Class- leafs (root/children) = nodes
class AVLTree:

    #AVLTree() -- Creates a new AVL Tree that is empty. It needs no parameters and returns an empty AVL Tree
    def __init__(self):
        self.root = None
        self.num = 0

    #size() -- Returns the number of items on the AVL Tree. It needs no parameters and returns an integer.
    def __len__(self):
        return self.num

    #is_empty() -- Tests to see whether the AVL Tree is empty. It needs no parameters and returns a boolean value.
    def is_empty(self):
        return self.num == 0

    #getter function to return height of a given node
    def get_height(self, node):
        if not node:
            return -1
        return node.height

    #function to calculate the balance of a particular tree (difference in height)
    def balanced(self, node):
        if not node:
            return 0
        return self.get_height(node.leftChild) - self.get_height(node.rightChild)


    #function to perform a righty rotation --> 1-2-3 --> 2-1-3
    def rightRotation(self, node):
        #temporary storing right/left
        left = node.leftChild
        right = left.rightChild

        #adjusting
        left.rightChild = node
        node.leftChild = right

        #assigning heights --> max of subtrees
        node.height = max(self.get_height(node.leftChild), self.get_height(node.rightChild)) + 1
        left.height = max(self.get_height(left.leftChild), self.get_height(left.rightChild)) + 1

        #returning node
        return left

    #function to perform a left rotation 
    def leftRotation(self, node):
        #temporary storing right/left
        right = node.rightChild
        left = right.leftChild

        #adjusting
        right.leftChild = node
        node.rightChild = left

        #assigning heights --> max of subtrees
        node.height = max(self.get_height(node.leftChild), self.get_height(node.rightChild)) + 1
        right.height = max(self.get_height(right.leftChild), self.get_height(right.rightChild)) + 1
        
        #returning node
        return right
 

  #insert(item) -- Adds a new item to the tree in it's approrpiate spot. It needs the item and returns nothing
    def insert(self, item):
        #increment. use helper function to assign root
        self.num = self.num + 1
        self.root = self.insertHelper(item, self.root)

#helper function to assign root
    def insertHelper(self, item, node):
        #base case
        if not node:
            return Node(item)

        #looking for left slot
        if item < node.data:
            node.leftChild = self.insertHelper(item, node.leftChild)
        else:
            #looking for right slot
            node.rightChild = self.insertHelper(item, node.rightChild)

        #assigning height --> max of subtrees
        node.height = max(self.get_height(node.leftChild), self.get_height(node.rightChild)) + 1

        #rotation before finalizing insertion- using rotate method
        return self.rotate(item, node)


#rotates tree to maintain balance
    def rotate(self, item, node):
        balance = self.balanced(node)
        ##RR rotation
        if balance > 1 and item < node.leftChild.data:

            return self.rightRotation(node)

        ##LL ROTATION
        if balance < -1 and item > node.rightChild.data:
            
            return self.leftRotation(node)

        #LR ROTATION
        if balance > 1 and item > node.leftChild.data:
          
            node.leftChild = self.leftRotation(node.leftChild)
            return self.rightRotation(node)

        #RL ROTATION
        if balance < -1 and item < node.rightChild.data:

            node.rightChild = self.rightRotation(node.rightChild)
            return self.leftRotation(node)

        #returning node
        return node 


    #depth-first search, recursive 
    #find(item) -- Tests to see if the specified item is in the tree. It needs the item and returns a boolean value.
    def find(self, item, node=None):

        if node == None:
            node = self.root

        #base case- true- found

        if node.data == item:
            return True

        #recursively checking left/right
        if item < node.data:
            if node.leftChild != None and node.leftChild.data != None:
                return self.find(item,node.leftChild)
            else:
                #false if there is no left child and we know it is left
                return False

        if item > node.data:
            if node.rightChild != None and node.rightChild.data != None:
                return self.find(item,node.rightChild)
            else:
                #false if there is no right child and we know it is more
                return False


    #helper method to find rightmost node     
    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node

    #delete(item) -- Removes the specified item from the tree and maintains avl tree intregrity. It needs the item and returns nothing. The tree is modified
    #uses helper method- delete node
    def delete(self, data):
        self.num = self.num - 1
        if self.root:
            #call helper
            self.root = self.deleteNode(data, self.root)

#helper method, removes node
    def deleteNode(self, item, node):

        #making sure there is a node to remove
        if not node:
            return node

        #finding node 
        if item < node.data:
            node.leftChild = self.deleteNode(item, node.leftChild)
        elif item > node.data:
            node.rightChild = self.deleteNode(item, node.rightChild)
        else:
            #node is FOUND

            #no children case- remove node
            if not node.leftChild and not node.rightChild:
                return None

            #one child case- remove linkage
            if not node.leftChild:
                return node.rightChild
            elif not node.rightChild:
                return node.leftChild

            #two children case- switching with rightmost
            tempNode = self.getMax(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.deleteNode(tempNode.data, node.leftChild)

        if not node:
            return node


        #re-balancing
        node.height = max(self.get_height(node.leftChild), self.get_height(node.rightChild)) + 1
        balance = self.balanced(node) 

        if balance > 1 and self.balanced(node.leftChild) >= 0:
            return self.rightRotation(node)

        if balance > 1 and self.balanced(node.leftChild) < 0:
            node.leftChild = self.leftRotation(node.leftChild)
            return self.rightRotation(node)

        if balance < -1 and self.balanced(node.rightChild) <= 0:
            return self.leftRotation(node)

        if balance < -1 and self.balanced(node.rightChild) > 0:
            node.rightChild = self.rightRotation(node.rightChild)
            return self.leftRotation(node)

        #return final 
        return node


    #string helper method- recursively covers all and adds to product array
    def toString(self, product=[], node=None):
        
        #base
        if node == None:
            node = self.root
        #What happens if root is None?
        if node != None:
            #append current
            product.append((node.data, node.height+1))
        pass

        #add left
        if node != None and node.leftChild and node.leftChild != None:
            self.toString(product, node.leftChild)

        #add right 
        if node != None and node.rightChild and node.rightChild != None:
            self.toString(product, node.rightChild)
    
        #return final product
        return str(product)


    #str() -- Returns a string of the AVL Tree and it's contents, formatted like a list of tuples of value and height in-order of top to bottom, left to right.
    #ie. [(19,3), (2,1), (107,2), (36,1), (108,1)]

    def __str__(self):
        return self.toString([])
        

# #TESTING

# #create new tree
# avl = AVLTree()

# print(avl.is_empty())
# #EXPECTED = TRUE

# avl.insert(10)
# avl.insert(20)
# avl.insert(30)
# avl.insert(40)
# avl.insert(50)
# avl.delete(10)
# print(len(avl))
# #EXPECTED = 4

# print(str(avl))
# #EXPECTED = [(40, 3), (20, 2), (30, 1), (50, 1)]
# avl.delete(20)
# avl.delete(40)
# avl.delete(50)
# avl.insert(60)
# avl.insert(70)
# avl.insert(80)
# avl.insert(90)
# avl.insert(100)
# avl.delete(100)

# print(len(avl))
# #EXPECTED = 5
# print(avl.is_empty())
# #EXPECTED = FALSE

# print(str(avl))
# #EXPECTED = [(40, 3), (20, 2), (30, 1), (50, 1), (80, 3), (60, 2), (30, 1), (70, 1), (90, 1)]
# print(avl.find(20))
# #EXPECTED = FALSE
# print(avl.find(80))
# #EXPECTED = TRUE


