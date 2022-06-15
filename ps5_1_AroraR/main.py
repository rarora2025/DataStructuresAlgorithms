"""
Implement a stack using linked lists.
You will want to import your ps4_2 code as a starting point (but leave it in a seperate file). Please let me know if you need help with this. Depending on your implementation, you may need to make changes to your code to achieve the objectives.

Your Stack class should be able to use the following methods:

#ListStack() -- Creates a new stack that is empty. It needs no parameters and returns an empty stack
    
#push(item) -- Adds a new item to the top of the stack. It needs the item and returns nothing
    
#pop() -- Removes the top item from the stack. It needs no parameters and returns the item. The stack is modified
    
#peek() -- Returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified
    
#is_empty() -- Tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    
#size() -- Returns the number of items on the stack. It needs no parameters and returns an integer.
    
#str() -- Returns a string of the  stack and it's contents, formatted as a list

"""
from LinkedList import *

class ListStack():
    def __init__(self): 

    	#creating new linked list (list) object
        self.stack = List()

    def push(self, item):
    	#using linked list add function, to add item to beginning of list
        self.stack.add(item)

    def pop(self, item=0):
    	#removing the item and index, if not given then default to --using linked list made pop function
        return self.stack.pop(0)

    def peek(self):
    	#using value_at function linked list to return the first item in the list  
    	return self.stack.value_at(0)

    def is_empty(self):
    	#reurning if size is 0, using linked list function -- size()
    	return self.stack.size() == 0

    	#using linked list function size 
    def size(self):
    	return self.stack.size()

    	#using linked list string funciton 
    def __str__(self):
    	return str(self.stack)


    
        
        
