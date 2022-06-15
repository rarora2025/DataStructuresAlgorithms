'''
Implement the BinarySearchTree we discussed in class. There is no checkmycode for this problem set, so be sure to thoroughly test your code.

Your BinarySearchTree class should be able to use the following methods:

#BinarySearchTree() -- Creates a new BST that is empty. It needs no parameters and returns an empty BST
    
#insert(item) -- Adds a new item to the tree in it's approrpiate spot. It needs the item and returns nothing
    
#delete(item) -- Removes the specified item from the tree and maintains tree intregrity. It needs the item and returns nothing. The tree is modified
    
#find(item) -- Tests to see if the specified item is in the tree. It needs the item and returns a boolean value.
    
#is_empty() -- Tests to see whether the BST is empty. It needs no parameters and returns a boolean value.
    
#size() -- Returns the number of items on the BST. It needs no parameters and returns an integer.
    
#str() -- Returns a string of the BST and it's contents, formatted as a list in-order, top to bottom, left to right.

By: Rahul Arora

document, sufficient testing
'''
class BinarySearchTree:
	#using a base node for binary tree
	def __init__(self, item, left_child=None, right_child=None):
		self.__data = item
		self.left_child = None
		self.right_child = None
		self.__size = 1


	#size funciton
	def size(self):
		return self.__size


	#recursive string function
	def __str__(self):
		in_order = []

		#adding current node
		in_order.append(self.__data)

		#adding left child if it exsists
		if self.left_child != None:
			in_order.append(str(self.left_child))

		
		#recursively adding right child if it exsists
		if self.right_child != None:
			in_order.append(str(self.right_child))

			#returning on final recursive call
		return ', '.join(str(x) for x in in_order) 

	#insert function
	def insert(self, item):
 	
 		#checking to see if tree is empty, inserting at root node if this is the case
		if self.is_empty():
			self.__data = BinarySearchTree(item)
			self.__size = self.__size + 1
			
		else:


		#insert func from class 
			# #if not empty keep track of all current nodes (using array queue), then append where apprioate and add nodes back to tree
			# queue = []
			# queue.append(self)
			# while queue:
			# 	temp_node = queue.pop(0)
			# 	if temp_node.left_child:
			# 		queue.append(temp_node.left_child)
			# 	else:
			# 		new_node = BinaryTreeNode(item, temp_node)
			# 		temp_node.left_child = new_node
			# 		self.__size = self.__size + 1
			# 		break
			# 	pass

			# 	if temp_node.right_child:
			# 		queue.append(temp_node.right_child)
			# 	else:
			# 		new_node = BinaryTreeNode(item, None, temp_node)
			# 		temp_node.right_child = new_node
			# 		self.__size = self.__size + 1
			# 		break
			# 	pass
			# pass

			#recursive insert function, sees correct placement recursively then inserts 
			if self.__data == item:
				return

			#checking if less in resursive call
			if item < self.__data:
				if self.left_child != None:
					
					self.left_child.insert(item)
				else:
					#if left child doesn't exsist, then insert, increase size
					self.left_child = BinarySearchTree(item)
			
					self.__size = self.__size + 1
			else:
				if self.right_child != None:
			
					self.right_child.insert(item)
				else:
					#if right child doesn't exsist, then insert, increase size
					self.right_child = BinarySearchTree(item)
					self.__size = self.__size + 1

		pass
	pass

	#return is empty function binary tree
	def is_empty(self):
		return self.__size == 0
	pass

	#depth-first search, recursive 
	def find(self, item):
		#base case- true- found
		if self.__data == item:
			return True

		#recursively checking left/right
		if item < self.__data:
			if self.left_child != None:
				return self.left_child.find(item)
			else:
				#false if there is no left child and we know it is left
				return False

		if item > self.__data:
			if self.right_child != None:
				return self.right_child.find(item)
			else:
				#false if there is no right child and we know it is more
				return False


	#helper function (for delete) fo find the min of a subtree
	def min(self):
		#recursively checks left child until it doesnt exsist, in which case return the value
		if self.left_child == None:
			return self.__data
		return self.left_child.min()

	#delete function implemented
	def delete(self, item):

		#recursively looping to find value
		if item < self.__data:
			if self.left_child != None:
				self.left_child = self.left_child.delete(item)
		elif item > self.__data:
			if self.right_child != None:
				self.right_child = self.right_child.delete(item)
		else:
			#if it is an empty leaf, remove node
			if self.left_child == None and self.right_child == None:
				return None

			#if there is just one child, remove one linkage
			if self.left_child == None:
				return self.right_child
			if self.right_child == None:
				return self.right_child

			#accounting for two children- recursively replace with minnimum node using helper function
			minnimum = self.right_child.min()
			self.__data = minnimum
			self.right_child = self.right_child.delete(minnimum)

		return self

#THOROUGH TESTING:
x = BinarySearchTree(20)
x.insert(10)
x.insert(50)
x.insert(30)
x.insert(70)
print("Tree Size: " +str(x.size())+" (Should be 5 at this point)\r\n")
print(x) #expected: 20, 10, 50, 30, 70
print(x.find(30)) #expected true
print(x.find(20)) #expected true
print(x.find(150))#expected false
x.delete(10)
x.delete(50)
print(x) #20, 70, 30



