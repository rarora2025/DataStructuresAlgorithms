'''
PSET 5-2
Rahul Arora
Due Date: 4/12/2022

You have implemented a queue using a Python list, now implement a queue using linked lists.

You will want to import your ps4_2 code as a starting point (but leave it in a seperate file). Please let me know if you need help with this. Depending on your implementation, you may need to make changes to your code to meet objectives.

Your Queue class should be able to use the following methods:

#ListQueue() -- creates a new queue that is empty. It needs no parameters and returns an empty queue.
    
#enqueue(item) -- adds a new item to the rear of the queue. It needs the item and returns nothing.
    
#dequeue() -- removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    
#front() -- returns the front item. It needs no parameters and returns the item.
    
#is_empty() -- tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    
#size() -- returns the number of items in the queue. It needs no parameters and returns an integer.
    
#str() -- returns what is in the queue. It needs no parameters and returns a string.
'''

"""
Linked list with needed functions from PSET 4-2
"""
import checkmycode
class List:
    #constructor
    def __init__(self):
        self.__length = 0
        self.__head = self.Node()
    pass
    #size, number of nodes in LL
    def size(self):
        return self.__length
    pass

    def __str__(self):
        arr = []
        header = self.__head.getNext()
        while header != None:
            arr.append(int(header.getData()))
            header = header.getNext()

        return str(arr)
        
    def is_empty(self):
        return self.__head.getNext() == None
    pass

    #insert(pos,item) -- Adds a new item to the list at position pos. It needs the item and returns nothing. Make sure the item is not already in the list and there are enough existing items to have position pos.

    def insert(self, pos, item):
        self.__length = self.__length + 1
   
        # header = self.__head
        # while header.getNext() != None:

        #     header = header.getNext()

        if True:


            pos = pos+1
            if not self.__head:
                self.__head = Node(item, self.__head)
            else:
                ptr = self.__head
                count = 0 
                while count < pos-1 and ptr.getNext() != None:                    
                    ptr = ptr.getNext()
                    count = count + 1

                ptr.setNext(self.Node(item, ptr.getNext()))

#adds new item to beginning fo list
    def add(self, item):
        if True:
            if self.is_empty():
                self.__head.setNext(self.Node(item))
                self.__length += 1
            else:
                temp = self.Node(item, self.__head.getNext())
                self.__head.setNext(temp)
                self.__length += 1
            pass
    pass



    def pop(self, position=0):
      self.__length = self.__length - 1
      position = position + 2
      deleted = None

    
      if(position < 1):
        
        return self.__head.getData()
        self.__head = None
      elif (position == 1 and self.__head != None):
        

        nodeToDelete = self.__head
        deleted = self.__head.getData()
        self.__head = self.__head.getNext()
        nodeToDelete = None
        return deleted
      else:    
        

        temp = self.__head
        for i in range(1, position-1):
          if(temp != None):
            temp = temp.getNext()  
        

        if(temp != None and temp.getNext() != None):
          nodeToDelete = temp.getNext()
          deleted = temp.getNext().getData()
        
          temp.setNext(temp.getNext().getNext())
          nodeToDelete = None 
        
        return deleted
       

#index_of(item) -- Returns the position of item in the list. It needs the item and returns the index. Make sure the item is in the list.
    def append(self, item):
        self.__length = self.__length + 1
        if not self.__head:
            self.__head = Node(item, self.__head)
        else:
            ptr = self.__head
            while ptr.getNext():                    # traverse until ptr.next is None
                ptr = ptr.getNext()

            ptr.setNext(self.Node(item, ptr.getNext()))


    def index(self, item):
        current = -1
        header = self.__head
        got = False
        while header != None and not got:
            if header.getData() == item:
                got = True
            else:
                header = header.getNext()
                current += 1

        if not got:
            return -1
        else:
            return current

        #value_at(pos) -- Returns the item at a specified position in the list. It needs the position and returns the value. Make sure the position is valid.
    def value_at(self, pos):

        cur = self.__head
        total = 0
 
        while (cur):
            if (total == pos+1):
                return cur.getData()
            else:
                total = total + 1
                cur = cur.getNext()
 
 
        return -1


   
    #insert(pos,item) -- Adds a new item to the list at position pos. It needs the item and returns nothing. Make sure the item is not already in the list and there are enough existing items to have position pos.



#remove(item) - Removes the item from the list. It needs the item and modifies the list. 
  #Make sure the item is present in the list. Returns nothing.

    def remove(self, item):
        self.__length = self.__length-1
        header = self.__head
 
        if (header != None):
            if (header.getData() == item):
                self.__head = header.getNext()
                header = None
                return
 
        while(header != None):
            if header.getData() == item:
                break
            temp = header
            header = header.getNext()
 
        if(header == None):
            return
 
        temp.setNext(header.getNext())
 
        header = None
      
      

#searches for item in list
    def search(self, item):
        if self.is_empty():
            return False
        current = self.__head.getNext()
        for index in range(self.__length):
            if(current.getData() == item):
                return True
            else:
                current = current.getNext()
            pass

        return False
        
        
        
        
    #inner class for a node object
    class Node:
        #constructor

        def __init__(self, data=None, next=None):
            self.__data =data
            self.__next = next
        pass

        def __repr__(self):
            return str(self.__data)
        pass

        def __str__(self):
            return str(self.__data)
        pass

#getters
        def getData(self):
            return self.__data
        pass

        def getNext(self):
            return self.__next
        pass

#setters
        def setData(self, item):
            self.__data = item
        pass

        def setNext(self, new_node):
            self.__next = new_node
        pass
pass

'''
Implement the Queue ADT using a python list such that the rear of the queue is at the end of the list.
I have given you the constructor.

Your Queue class should include the following methods:
'''

#defining class

class ListQueue:

#constructor
#Queue() -- creates a new queue that is empty. It needs no parameters and returns an empty queue.
	def __init__(self):
		self.__list = List()
	pass

#enqueue(item) -- adds a new item to the rear of the queue. It needs the item and returns nothing.
	def enqueue(self, item):
		#appending to list
		self.__list.append(item)
	pass

#dequeue() -- removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
	def dequeue(self):
		return self.__list.pop(0)
        

#front() -- returns the front item. It needs no parameters and returns the item.
	def front(self):
		if (len(self.__list) > 0):
			#returning front using square brackets to access index
			return self.__list.value_at(0)
		return None
	pass

#is_empty() -- tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
	def is_empty(self):
		#evaluating wether size is 0
		return self.__list.size() == 0
	pass

#size() -- returns the number of items in the queue. It needs no parameters and returns an integer.
	def size(self):
		#returning size of list
		return self.__list.size()
	pass

#str() -- returns what is in the queue. It needs no parameters and returns a string.
	def __str__(self):
		#returning string form of list
		return str(self.__list)





