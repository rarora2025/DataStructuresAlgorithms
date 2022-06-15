'''
The linked list implementation you've implemented is called a singly linked list because each node has a single reference to the next node in sequence.

An alternative implementation we've discussed is known as a doubly linked list. In this implementation, each node has a reference to the successor node (commonly called next) as well as a reference to the predecessor node (commonly called prev). The head reference can also contain two references, one to the first node in the linked list and one to the last. Code this implementation in Python.

Your doubly linked list class should include the following methods:

#DoublyList() -- Creates a new list that is empty. It needs no parameters and creates an empty list.

#add(item) -- Adds a new item to the beginning of the list. It needs the item and returns nothing.

#append(item) -- Adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing.

#insert(pos,item) -- Adds a new item to the list at position pos. It needs the item and returns nothing. Make sure there are enough existing items to have position pos.

#remove(item) -- Removes the item from the list. It needs the item and modifies the list. 

#pop(pos) -- Removes and returns the item at position pos or the first item is no position is given. It needs the position and returns the item. 

#index_of(item) -- Returns the position of item in the list. It needs the item and returns the index. Make sure the item is in the list.

#value_at(pos) -- Returns the item at a specified position in the list. It needs the position and returns the value. Make sure the position is valid.

#search(item) -- Searches for the item in the list. It needs the item and returns a boolean value.

#is_empty() -- Tests to see whether the list is empty. It needs no parameters and returns a boolean value.

#size() -- Returns the number of items in the list. It needs no parameters and returns an integer.

#str() -- Returns a str of the doubly linked list from first to last and should include []

#reverse_str() -- Returns a str of the doubly linked list from last to first and should include []
'''