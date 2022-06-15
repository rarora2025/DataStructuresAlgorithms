"""
Description: Testing the Linked List
Original Author: Rahul Arora
"""

from UnorderedList import *
myLL = UnorderedList()
print("isEmpty(): true? " + str(myLL.isEmpty()))
print("size(): 0? " + str(myLL.size()))
myLL.add(2)
myLL.add(10)
myLL.add(5)

print("isEmpty(): false?: " + str(myLL.isEmpty()))
print("size(): 3? " + str(myLL.size()))


print("myLL= [5,10,2]? " + str(myLL))
print("pop(): 5?: " + str(myLL.pop()))


print("search(5): false?  "+ str(myLL.search(5)))
print("search(2): true? " + str(myLL.search(2)))
print("myLL= [10, 2]? " + str(myLL))

print("index of 2 = 1? " + str(myLL.index_of(2)))

print("value at index 1 = 2? " + str(myLL.value_at(1)))

myLL.remove(2)
print("after myLL.remove(2) = [10]? " + str(myLL))










