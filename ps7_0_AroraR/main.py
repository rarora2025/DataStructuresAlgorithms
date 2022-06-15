'''
Implement an SortedMap map class. 

I have given you a starting point with the BaseMap and UnsortedMap class but you will have to make changes to those methods we overwrote in your SortedMap. It should have all the functionailty we programmed but for sorted as well as the following functionality.


#k in M -- Return True if the map contains an item with key k. Need to implement __contains__ methods

#get(k) -- Return M[k] if key k exists in the map. If key k is not in the map raise KeyError

#set(k, v) -- If key k exists in the map, set M[k] = v and return M[k]; if key k is not in the map raise KeyError .

#pop(k) -- Remove the item associated with key k from the map and return its associated value v. If key k is not in the map raise KeyError

#popitem() -- Remove the first key-value pair from the map, and return a (k,v) tuple representing the removed pair. If map is empty raise IndexError

#clear() -- Remove all key-value pairs from the map.

#keys() -- Return a list of all keys of M.

#values() -- Return a list of all values of M.

#items() -- Return a list of (k,v) for all entries of M.

#merge(M2) -- Merge two maps together. Does not modify orignal maps. If a key exists in both maps, retain the value from M1 in new map. Return new merged map.

#size() -- Returns the number of entries in the map. It needs no parameters and returns an integer.

#str() -- Returns a string representation of the map and it's contents, formatted like a list of tuples of key and value.
ie. [(ham:1), (nice:100), (10:2), (45:1), (ball:1)] 


Use import checkmycode to make sure you are on the right track.
'''
from base_map import BaseMap
from sorted_map import SortedMap
import checkmycode
# s = SortedMap()
# s[0] = 3
# print(s.get(0))
# print(s.get(1))