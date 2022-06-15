#Sorted Map Class- making map
#Rahul Arora
#5/24/2022

#importing BaseMap class from file
from base_map import BaseMap

#UnsortedMap Class 
class SortedMap(BaseMap):

	#constructor
	def __init__(self):
		self.__map = []
	pass

	#functions- set, get, search, del, len (is_empty ?), str

	#returns- get method
	def __getitem__(self, k):
		for entry in self.__map:
			#look for matching key, return value
			if k == entry._key:
				return entry._value
			pass
		pass
		return None
	pass

#GET METHOD- REIMPLEMENTED BINARY
	def get(self, k):
		# for entry in self.__map:
		# 	if k == entry._key:
		# 		return entry._value
		# 	pass
		# pass
		# raise KeyError('Error: Key ' + k + ' not found in map')
		# return 
		return self.binary_get(self.__map, 0, len(self.__map)-1, k)
	
	def binary_get(self, arr, low, high, k):
	    # Check base case
	    if high >= low:
	 
	        mid = (high + low) // 2
	 
	        # If element is present at the middle itself
	        if arr[mid]._key == k:
	            return arr[mid]._value
	 
	        # If element is smaller than mid, then it can only
	        # be present in left subarray
	        elif arr[mid]._key > k:
	            return self.binary_get(arr, low, mid - 1, k)
	 
	        # Else the element can only be present in right subarray
	        else:
	            return self.binary_get(arr, mid + 1, high, k)
	 
	    else:
	        # Element is not present in the array
	        raise KeyError('Error: Key ' + str(k) + ' not found in map')
	        return

	#chagnes values of keys
	def __setitem__(self, k, v):
		for entry in self.__map:
			if k == entry._key:
				entry._value = v
				return
			pass
		pass
		index = 0
		if len(self.__map) > 0:
			for entry in self.__map:
				if entry < self._Map_Entry(k,v):
					index = index + 1
		
		self.__map.insert(index, self._Map_Entry(k,v))
	
	pass

		#chagnes values of keys
	def set(self, k, v):
		for entry in self.__map:
			if k == entry._key:
				entry._value = v
				return
			pass
		pass
		raise KeyError('Error: Key ' + k + ' not found in map')
	pass

	def binary_del(self, arr, low, high, k):
	    # Check base case
	    if high >= low:
	 
	        mid = (high + low) // 2
	 
	        # If element is present at the middle itself
	        if arr[mid]._key == k:
	            arr.pop(mid)
	            return True
	 
	        # If element is smaller than mid, then it can only
	        # be present in left subarray
	        elif arr[mid]._key > k:
	            return self.binary_del(arr, low, mid - 1, k)
	 
	        # Else the element can only be present in right subarray
	        else:
	            return self.binary_del(arr, mid + 1, high, k)
	 
	    else:
	        # Element is not present in the array
	        return False

	#deletes
	def __delitem__(self, k):
		return self.binary_del(self.__map, 0, len(self.__map)-1, k)
		# for i in range(len(self.__map)):
		# 	if k == self.__map[i]._key:
		# 		self.__map.pop(i)
		# 		return True
		# 	pass
		# pass
		# return False

#POP METHOD- REIMPLEMENTED BINARY
	def binary_pop(self, arr, low, high, k):
	    # Check base case
	    if high >= low:
	 
	        mid = (high + low) // 2
	 
	        # If element is present at the middle itself
	        if arr[mid]._key == k:
	            return arr.pop(mid)._value
	 
	        # If element is smaller than mid, then it can only
	        # be present in left subarray
	        elif arr[mid]._key > k:
	            return self.binary_pop(arr, low, mid - 1, k)
	 
	        # Else the element can only be present in right subarray
	        else:
	            return self.binary_pop(arr, mid + 1, high, k)
	 
	    else:
	        # Element is not present in the array
	        raise KeyError('Error: Key ' + str(k) + ' not found in map')
	        return


	#deletes
	def pop(self, k):
		return self.binary_pop(self.__map, 0, len(self.__map)-1, k)
		# for i in range(len(self.__map)):
		# 	if k == self.__map[i]._key:
		# 		return str(self.__map.pop(i)._value)
				
		# 	pass
		# pass
		# raise KeyError('Error: Key ' + str(k) + ' not found in map')
	pass

	#deletes
	def popitem(self):
		if len(self.__map) == 0:
			raise IndexError("Error: Map has no entries")
		else:
			popped = self.__map.pop(0)
			return "(\'" + str(popped._key) + "\', " + str(popped._value) + ")"
			#('france', 45)

	pass

	def clear(self):
		self.__map = []

	def keys(self):
		keys = []
		for entry in self.__map:
			keys.append(entry._key)

		return keys

	def values(self):
		vals = []
		for entry in self.__map:
			vals.append(entry._value)

		return vals

	def items(self):
		items = []
		largestring = "["
		for entry in range(len(self.__map)):
			popped = self.__map[entry]
			largestring += "(\'" + str(popped._key) + "\', " + str(popped._value) + ")"
			if entry < len(self.__map) - 1:
				largestring += ", "
			else:
				largestring += "]"

			

		return largestring
	def size(self):
		return len(self.__map)

	#returns size
	def __len__(self):
		return len(self.__map)
	pass

	#allows to be iterable
	def __iter__(self):
		return iter(self.__map)
	pass

	#returns if map is empty
	def is_empty(self):
		return len(self.__map) == 0
	pass

	#returns formatted string of map
	def __str__(self):
		count = len(self.__map)
		s = "{"
		for entry in self.__map:
			s += str(entry)
			count -= 1
			if count >= 1:
				s += ", "
			pass
		pass
		s += "}"
		return s
	pass

#POP METHOD- REIMPLEMENTED BINARY
	def binary_search(self, arr, low, high, k):
	    # Check base case
	    if high >= low:
	 
	        mid = (high + low) // 2
	 
	        # If element is present at the middle itself
	        if arr[mid]._key == k:
	            return True
	 
	        # If element is smaller than mid, then it can only
	        # be present in left subarray
	        elif arr[mid]._key > k:
	            return self.binary_search(arr, low, mid - 1, k)
	 
	        # Else the element can only be present in right subarray
	        else:
	            return self.binary_search(arr, mid + 1, high, k)
	 
	    else:
	        # Element is not present in the array
	        return False

#looking if key in 
	def __contains__(self, k):
		return self.binary_search(self.__map, 0, len(self.__map)-1, k)
		# for i in range(len(self.__map)):
		# 	if k == self.__map[i]._key:
		# 		return True
		# 	pass
		# pass
		# return False

#merge(M2) -- Merge two maps together. Does not modify orignal maps. If a key exists in both maps, retain the value from M1 in new map. Return new merged map.
	def merge(self, M2):
		merged_map = []
		for entry in M2:
			merged_map.append(entry)
		for entry in self.__map:
			merged_map.append(entry)
		
		s = SortedMap()
		for index in range(len(merged_map)):
			s[merged_map[index]._key] = merged_map[index]._value
		return s



