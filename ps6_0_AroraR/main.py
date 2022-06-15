"""
By: Rahul Arora 
Binary Tree with Depth/Breath Search/toString Implemented
"""


# #using a base node for binary tree
# class Node:
# 	#constructor
# 	def __init__(self, item, parent = None, left_child = None, right_child = None):
		
# 		self.__data = item
# 		self.parent = parent
# 		self.left_child = left_child
# 		self.right_child = right_child
# 		self.children = []

# 	def __repr__(self):
# 		return str(self.__data)
# 	pass

# 	def __str__(self):
# 		return str(self.__data)
# 	pass

# 	#getters
# 	def getData(self):
# 		return self.__data
# 	pass

# 	#setters
# 	def setData(self, item):
# 		self.__data = item
# 	pass

# 	def setNext(self, new_node):
# 		self.__next = new_node
# 	pass


#binary tree	
class BinaryTree:
	#using a base node for binary tree
	class Node:
		#constructor
		def __init__(self, item, parent = None, left_child = None, right_child = None):
			
			self.__data = item
			self.parent = parent
			self.left_child = left_child
			self.right_child = right_child
			self.children = []

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

		#setters
		def setData(self, item):
			self.__data = item
		pass

		def setNext(self, new_node):
			self.__next = new_node
		pass

	#insert function
	def insert(self, item):
		#append item to children array
		# self.__root.children.append(item)
		#if tree empty, make item node and return 
		if self.is_empty():
			self.__root = self.Node(item)
			self.__size = self.__size + 1
		else:
			#if not empty keep track of all current nodes (using array queue), then append where apprioate and add nodes back to tree
			queue = []
			queue.append(self.__root)
			while queue:
				temp_node = queue.pop(0)
				if temp_node.left_child:
					queue.append(temp_node.left_child)
				else:
					new_node = self.Node(item, temp_node)
					temp_node.left_child = new_node
					self.__size = self.__size + 1
					break
				pass

				if temp_node.right_child:
					queue.append(temp_node.right_child)
				else:
					new_node = self.Node(item, temp_node)
					temp_node.right_child = new_node
					self.__size = self.__size + 1
					break
				pass
			pass
		pass
	pass

	#breadth first
	def breadth_search(self, item):
		#original root
		node = self.__root
		
		#when node is there, check node, right, and left
		while node != None:
			if node.getData() == item:
				return True

			if node.left_child != None:
				node = node.left_child

			if(node.getData() == item):
				return True

			if node.right_child != None:
				node = node.right_child

			if(node.getData() == item):
				return True

			return False

#return false if not found
		

	#depth first
	def depth_search(self, item, root=None): 

		#default to root
		if not root:
			root = self.__root

			#check root
		if root.getData() == item:
			return True
		else:

			#recursively check all right/left children (making them central nodes)
			if root.right_child:
				return self.depth_search(item, root.right_child)
			elif root.left_child:
				return self.depth_search(item, root.left_child) 
			else:
				#false if not found
				return False
		


#to string method- converts tree to string
	def toString(self, root=None, string=""):
		#initially string is empty, if this then set root to central node root
		if string == "":
			root = self.__root

		if root:
			#if root exsists, add it  (intially dont add new line)
			if string == "":
				string = string + str(root.getData())
			else:
				string = string + "\n" + str(root.getData())

#if children exsists, add them recursively
		if root.right_child:
			return self.toString(root.right_child, string)
		elif root.left_child:
			return self.toString(root.left_child, string )
		else:
			return string

#initial init for binary tree
	def __init__(self):
		self.__size = 0
		self.__root = None
	pass

	

#return size
	def __len__(self):
		return self.__size
	pass

#return is empty function binary tree
	def is_empty(self):
		return self.__size == 0
	pass



#TESTING
# tree = BinaryTree(99)
# tree.insert(1)
# print(tree.toString())
# print(tree.breadth_search(99))
# print(tree.depth_search(1))
# print(tree.depth_search(100))
# print(tree.breadth_search(2))

#expected output 
"""
99
1
True
True
False
False
"""
