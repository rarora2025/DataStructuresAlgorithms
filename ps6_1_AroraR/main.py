'''
Implement the delete method for the BinaryTree class we created together in class. There is no checkmycode for this problem set, so be sure to thoroughly test your code.
'''

"""
By: Rahul Arora 
5/22/2022
Binary Tree w/ Delete Function
"""

#Node class- base node
class Node:
	def __init__(self, item, left_child=None, right_child=None):
		self.__data = item
		self.left_child = None
		self.right_child = None

	def getData(self):
		return self.__data

	def setData(self, item):
		self.__data = item

#binary tree	
class BinaryTree:
	#constructor
	def __init__(self):
		self.__size = 0
		self.__root = None

	#size funciton
	def __len__(self):
		return self.__size


	#recursive string function
	def toString(self, node=None):
		in_order = []

		if node == None:
			node = self.__root

		#need to check if root is None
		if node == None:
			return str(in_order)
	
		if node.getData() != None:
			in_order.append(node.getData())

		#adding left child if it exsists
		if node.left_child != None and node.left_child.getData() != None:
			in_order.append(self.toString(node.left_child))

		
		#recursively adding right child if it exsists
		if node.right_child != None and node.right_child.getData() != None:
			in_order.append(self.toString(node.right_child))

			#returning on final recursive call
		return ', '.join(str(x) for x in in_order) 

	#You should of had a __str__ method
	def __str__(self):
		return self.toString()
	pass


	#delete function
	def delete(self, item, root1=None, root2=None, foundRight=False):
		#when found the max root, find node to delete
		if foundRight:
			#finding node to delete
			#print(root2.getData())


			if root1 == None:
				root1 = self.__root

			#print(root1.getData())

			#found node to delete, switch them 
			if root1.getData() == item:
				root1.setData(root2.getData())
				root2.setData(None)
				self.__size = self.__size - 1
				
			else:


				#recursively check all right/left children (making them central nodes)
				if root1.right_child and root1.right_child.getData() != None:
					self.delete(item, root1.right_child, root2, True)
				

				if root1.left_child and root1.left_child.getData() != None:
					self.delete(item, root1.left_child, root2, True) 
				

		else:
			#looking for node to switch with 
			if root2 == None:
				#default - start rightmost at root
				root2 = self.__root

			if root2.right_child == None or root2.right_child.getData() == None:
				if root2.left_child != None and root2.left_child.getData() != None:
					self.delete(item, root1, root2.left_child, False)
				#checking left child --> if you just switched the right child to None then it will still say that the right child holds an object
				else:
					#recursive call when found
					self.delete(item, root1, root2, True)
			else:
				#recursive call when not found
				self.delete(item, root1, root2.right_child, False)



	#insert function (from class)
	def insert(self, item):
		
		#if tree empty, make item node and return 
		if self.is_empty():
			self.__root = Node(item)
			self.__size = 1
		else:
			#if not empty keep track of all current nodes (using array queue), then append where apprioate and add nodes back to tree
			queue = []
			queue.append(self.__root)
			while queue:
				temp_node = queue.pop(0)
				if temp_node.left_child:
					queue.append(temp_node.left_child)
				else:
					new_node = Node(item)
					temp_node.left_child = new_node
					self.__size = self.__size + 1
					break
				pass

				if temp_node.right_child:
					queue.append(temp_node.right_child)
				else:
					new_node = Node(item)
					temp_node.right_child = new_node
					self.__size = self.__size + 1
					break


	#return is empty function binary tree
	def is_empty(self):
		return self.__size == 0
	pass




# #THOROUGH TESTING:
# x = BinaryTree(0)
# x.insert(1)
# x.insert(2)
# x.insert(3)
# x.insert(4)
# x.insert(5)
# x.insert(6)
# x.insert(7)
# x.insert(8)
# print(x.toString())
# #EXPECTED = 0, 1, 3, 7, 8, 4, 2, 5, 6

# x.delete(6)
# x.delete(5)
# x.delete(4)
# print(x.toString())
# #EXPECTED = 0, 1, 3, 7, 8, 2

# x.insert(9)
# x.insert(10)
# print(x.toString())
# #EXPECTED = 0, 1, 3, 7, 8, 2, 9, 10

